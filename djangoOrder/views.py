from django.core.exceptions import ValidationError
from django.shortcuts import render,redirect

from Products.models import Product
from .forms import orderForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import Order

@login_required(login_url="/login")
def add_user_order(request):
    form=orderForm(request.POST or None)
    if form.is_valid():
        order=Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
        if order is None:
            order = Order.objects.create(owner=request.user, is_paid=False)
        productID=form.cleaned_data.get("productID")
        count=form.cleaned_data.get("order_Count")
        if count < 1:
            count = 1
        product=Product.objects.get_by_id(productID)
        order.order_detail_set.create(product_id=productID,price=product.price,count=count)
        return redirect("home")
    else:
        return ValidationError("مشکلی رخ داده!لطفا دوباره امتحان کنید.")

@login_required(login_url="/login")
def user_open_order(request):
    context={
    "order":None,
    "details":None
    }
    order:Order=Order.objects.filter(is_paid=False,owner_id=request.user.id).first()
    if order is not None:
        context["order"]=order
        context["details"]=order.order_detail_set.all()
    return render(request,"user_open_order.html",context)

@login_required(login_url="/login")
def delete_order_detail(request):
    detail_id=request.POST.get("productID")
    open_order:Order=Order.objects.filter(owner_id=request.user.id,is_paid=False).first()
    if open_order is not None:
        open_order.order_detail_set.filter(id=detail_id).delete()
    return redirect("djangoOrder:Order")