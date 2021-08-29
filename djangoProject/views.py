from django.shortcuts import render,redirect


def home_page(request):
    context={
        "data":"data"
    }
    return render(request,"home_page.html",context)

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