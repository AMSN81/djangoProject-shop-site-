from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from Products.models import Product


class Order(models.Model):
    owner=models.ForeignKey(to=User,on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)
    payment_date=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.owner.get_username()

class Order_Detail(models.Model):
    order=models.ForeignKey(to=Order,on_delete=models.CASCADE)
    product=models.ForeignKey(to=Product,on_delete=models.CASCADE)
    price=models.IntegerField()
    count=models.IntegerField()

    def __str__(self):
        return f"{self.product.title}*{self.count}"

    def get_detail_sum(self):
        return self.price*self.count


