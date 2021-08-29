"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from djangoProject import settings


from .views import (home_page,header,footer,footer_refrence,header_refrence)

urlpatterns = [
    path('', home_page,name="home"),
    path('header', header ,name="header"),
    path('footer', footer ,name="footer"),
    path('footer_ref', footer_refrence ,name="footer_refrence"),
    path('header_ref', header_refrence ,name="header_refrence"),
    path('admin/', admin.site.urls),
    path('', include("djangoAccount.urls",namespace="account")),
]
if settings.DEBUG:
    urlpatterns=urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
