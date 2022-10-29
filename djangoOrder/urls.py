from django.urls import path

from djangoOrder.views import add_user_order, user_open_order , delete_order_detail

app_name="djangoOrder"

urlpatterns = [
    path('add_user_order',add_user_order),
    path('order',user_open_order,name="Order"),
    path('delete_order_detail',delete_order_detail,name="delete_order_detail"),
    ]