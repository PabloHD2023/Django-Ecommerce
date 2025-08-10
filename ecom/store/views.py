from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.

def category(request, foo):
    # Replace hyphens with spaces in the category name
    foo = foo.replace('-', ' ')
    # Get the category object
    try:
        category = Category.objects.get(name=foo)
    except Category.DoesNotExist:
        messages.error(request, "Category not found.")
        return redirect('home')
    
    # Get all products in that category
    products = Product.objects.filter(category=category)
    
    return render(request, 'category.html', {'category': category, 'products': products})

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Se ha conectado correctamente.")
            return redirect('home')
        else:
            messages.error(request, "La password o el usuario son incorrectos.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "Se ha desconectado correctamente.")
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            # Authenticate and log in the user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Usuario registrado correctamente.")
            return redirect('home')
        else:
            messages.error(request, "Error al registrar el usuario. Por favor, corrige los errores.")
            return render('register')
    else:
        return render(request, 'register.html', {'form': form})
    

def product(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product.html', {'product': product})