from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import login_form,register_form
from django.contrib.auth.models import User
# Create your views here.

def logout_page(request):
    logout(request)
    return redirect("home")


def login_page(request,*args,**kwargs):
    form = login_form(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            print("error")

    return render(request,"account/login.html",context)

def register_page(request,*args,**kwargs):
    form = register_form(data=request.POST)
    context={
        "form":form
    }
    if form.is_valid():
        print("gg")
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        email=form.cleaned_data.get("email")
        new_user=User.objects.create_user(username=username,password=password,email=email)
        login(request,new_user)
        return redirect("home")
    else:
        print("wtfffffffffffffffffff")

    return render(request,"account/register.html",context)
