"""firstProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from accounts.views import (
    login_view,
    logout_view,
    register_view,
)
from products.views import (
    home_view,
    search_view,
    Product_detail_view,
    Product_api_detail_view,
    Product_list_view,
    product_create_view,
)


urlpatterns = [
    path('',home_view),

    path('login/',login_view),
    path('accounts/login/',login_view),
    path('logout/',logout_view),
    path('register/',register_view),


    path('search/',search_view),
    path('products/',Product_list_view),
    path('products/<int:pk>/',Product_detail_view),
    # path('products/1/',Product_detail_view),
    path('forms/',product_create_view),
    path('api/products/<int:pk>/',Product_api_detail_view),
    path('admin/', admin.site.urls)
]

