from django.db.models import Q
from django.db import models
from django.http import Http404

from djangoCategory.models import Categories
import os

# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return name , ext

def upload_img(instance,filename):
    name , ext = get_filename_ext(filename)
    print(instance.id)
    final_name= f"{instance.id}-{instance.title}{ext}"
    return f"Products/{final_name}"

def upload_img_gallery(instance,filename):
    name , ext = get_filename_ext(filename)
    final_name= f"{instance.id}-{instance.title}{ext}"
    return f"Products/Gallery/{final_name}"

class productManager(models.Manager):
    def get_active(self):
        return self.get_queryset().filter(active=True)
    def get_by_id(self,Pid):
        return self.get_active().filter(id=Pid).first()
    def get_by_category(self,category_name):
        return Product.objects.filter(categories__title__iexact=category_name)


    def search(self,search):
        lookup=(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(tag__title__icontains=search)
        )
        return self.get_active().filter(lookup).distinct()

class Product(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField()
    price=models.DecimalField(max_digits=20,decimal_places=2,default=10)
    image=models.ImageField(upload_to=upload_img, null=True , blank=True)
    active=models.BooleanField(default=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    categories=models.ManyToManyField(Categories,blank=True)
    ad_in_home=models.BooleanField(default=False)

    objects = productManager()

    def __str__(self):
        return self.title

    def get_url(self):
        return f"/product/{self.id}"

class ProductGallery(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_img_gallery, null=True, blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name_plural="Galleries"
