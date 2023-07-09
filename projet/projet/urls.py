from django.urls import path
from app import views

urlpatterns = [
    path('', views.index, name="index"),
    path('homeBack', views.homeBack, name="homeBack"),
    path('blog-5/', views.blog5, name="blog5"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('error-404/', views.error404, name="error404"),
    path('login/', views.login, name="login"),
    path('products-left-sidebar-2/', views.productLeftSideBar2, name="productLeftSideBar2"),
    path('products-type-1/', views.productsType1, name="productsType1"),
    path('signup/', views.signup, name="signup"),
    path('single-blog-1/', views.singleBlog1, name="singleBlog1"),
    path('track-order/', views.trackOrder, name="trackOrder"),
]
