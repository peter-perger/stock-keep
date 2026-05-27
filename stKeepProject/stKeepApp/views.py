from django.shortcuts import render, redirect
from .forms import RegisterForm

from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def index_view(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        
  
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