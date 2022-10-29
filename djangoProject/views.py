from django.shortcuts import render,redirect
from Products.models import Product


def home_page(request):
    product=Product.objects.get_queryset().filter(ad_in_home=True)
    context={
        "product":product,
        "data":"data"
    }
    return render(request,"home_page.html",context)

def about_page(request):
    context={

    }
    return render(request,"about_page.html",context)


def header(request, *args, **kwargs):
    context={
        "data":"data"
    }
    return render(request,"Shared/header.html",context)

def footer(request, *args, **kwargs):
    context={
        "data":"data"
    }
    return render(request,"Shared/footer.html",context)

def footer_refrence(request, *args, **kwargs):
    context={
        "data":"data"
    }
    return render(request,"Shared/footer_refrence.html",context)

def header_refrence(request, *args, **kwargs):
    context={
        "data":"data"
    }
    return render(request,"Shared/header_refrence.html",context)