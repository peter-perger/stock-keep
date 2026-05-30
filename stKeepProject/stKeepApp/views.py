from django.shortcuts import render, redirect
from .forms import RegisterForm, AddProductForm

from django.views import View

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def index_view(request):
    return render(request, 'index.html')


def login_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = "Invalid username or password"
        
    context = {"error_message": error_message}

    return render(request, 'login.html', context=context)


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')

            user = User.objects.create_user(username=username, email=email, password=password)
            login(request=request, user=user)
            return redirect('index')

    else:
        form = RegisterForm()
    
    context = {'form': form}
    return render(request, 'register.html', context=context)


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
    
    else:
        return render(request, 'logout.html')


class ProfileView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    # 'next' - to redirect URL
    redirect_field_name = 'next'

    def get(self, request):
        return render(request, 'profile.html')
    

class AddProductView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'next'

   
    def get(self, request):
            form = AddProductForm()
            context = {'form': form}

            return render(request, 'add-product.html', context=context)
    
    def post(self, request):
        form = AddProductForm(request.POST)

        if form.is_valid():
            product = form.save()
            product.managed_by = request.user
            product.save()

            return redirect("index")
        else:
            return render(request, 'add-product.html', {'form': form})