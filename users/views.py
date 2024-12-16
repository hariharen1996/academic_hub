from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegistrationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account created for username: {username}")
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request,"users/register.html",{"form":form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,f"LoggedIn with username: {username}")
                return redirect('home')
           
    else:
        form = AuthenticationForm()
    return render(request,"users/login.html",{'form':form})   
            