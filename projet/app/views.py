from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from .forms import SignupForm
from .models import Profile# Create your views here.
# XXXXX FRONT XXXXX
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



def productLeftSideBar2(request):
    return render(request, 'app/front/main/products-left-sidebar-2.html')

def productsType1(request):
    return render(request, 'app/front/main/products-type-1.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'member'  # Définir le rôle de l'utilisateur en tant que membre
            user.password=make_password(form.cleaned_data['password'])
            user.save()
            login(request,user)
            return redirect('index')  # Rediriger vers la page d'accueil après l'inscription
            
    else:
        form = SignupForm()
    return render(request, 'app/front/main/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = "Nom d'utilisateur ou mot de passe incorrect."
            return render(request, 'app/front/main/login.html', {'error_message': error_message})
    else:
        return render(request, 'app/front/main/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def singleBlog1(request):
    return render(request, 'app/front/main/single-blog-1.html')

def trackOrder(request):
    return render(request, 'app/front/main/track-order.html')

# XXXXX BACK XXXXX
def homeBack(request):
    return render(request, 'app/back/main/homeBack.html')