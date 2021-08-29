from django.urls import path
from .views import login_page,register_page,logout_page
app_name="djangoAccount"

urlpatterns = [
    path('login',login_page,name="login"),
    path('logout',logout_page,name="logout"),
    path('register',register_page,name="register"),
    ]
