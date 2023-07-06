from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'app/front/main/index.html')

def blog5(request):
    return render(request, 'app/front/main/blog-5.html')

def cart(request):
    return render(request, 'app/front/main/cart.html')

def checkout(request):
    return render(request, 'app/front/main/checkout.html')

def contact(request):
    return render(request, 'app/front/main/contact.html')

def error404(request):
    return render(request, 'app/front/main/error-404.html')

def login(request):
    return render(request, 'app/front/main/login.html')

def productLeftSideBar2(request):
    return render(request, 'app/front/main/product-left-sidebar-2.html')

def productsType1(request):
    return render(request, 'app/front/main/products-type-1.html')

def signup(request):
    return render(request, 'app/front/main/signup.html')

def singleBlog1(request):
    return render(request, 'app/front/main/single-blog-1.html')

def trackOrder(request):
    return render(request, 'app/front/main/track-order.html')

