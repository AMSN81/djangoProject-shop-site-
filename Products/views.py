import itertools

from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from Products.models import Product,ProductGallery
from djangoCategory.models import Categories
from djangoOrder.forms import orderForm


class product_list(ListView):
    template_name = "products_list.html"
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.get_active()

class product_by_category(ListView):
    template_name = "products_list.html"
    paginate_by = 6

    def get_queryset(self):
        category_name=self.kwargs["category_name"]
        print(category_name)
        c=Categories.objects.filter(address__iexact=category_name).first()
        if c is None:
            raise Http404
        return Product.objects.get_by_category(category_name)

def my_grouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e is not None] for t in itertools.zip_longest(*args))

def product_detail(request,*args,**kwargs):
    print(kwargs)
    Pid=kwargs["id"]
    form = orderForm(request.POST or None,initial={'productID':Pid})
    product=Product.objects.get_by_id(Pid)
    del_id=[Pid]
    print(product)
    pre_gallery=ProductGallery.objects.filter(product__id=Pid)
    gallery=my_grouper(3,pre_gallery)
    related_products=Product.objects.get_queryset().filter(categories__product=product)
    if product in related_products:
        print(product)
        print(related_products)
    rel=my_grouper(3,related_products)
    context={
        'gallery' : gallery,
        'product' : product,
        'rel':rel,
        'orderForm':form,
    }
    return render(request,"product_detail.html",context)

class search_item(ListView):
    template_name = "products_list.html"
    paginate_by = 6

    def get_queryset(self):
        search=self.request.GET.get("q")
        return Product.objects.search(search=search)

def Categories_list_partial_view(request):
    categories=Categories.objects.all()
    context={
        "categories":categories,
    }
    return render(request,"Catrgories_list.html" ,context)