"""
URL configuration for azz project.

The  list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('blog-5/', views.blog5, name="blog5"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('error-404/', views.error404, name="error404"),
    path('login/', views.login, name="login"),
    path('product-left-sidebar-2/', views.productLeftSideBar2, name="productLeftSideBar2"),
    path('products-type-1/', views.productsType1, name="productsType1"),
    path('signup/', views.signup, name="signup"),
    path('single-blog-1/', views.singleBlog1, name="singleBlog1"),
    path('track-order/', views.trackOrder, name="trackOrder"),
]
