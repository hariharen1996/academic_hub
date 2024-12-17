from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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
            
@login_required            
def logout_user(request):
    logout(request)
    messages.warning(request,f"You have been logged out!😕")
    return redirect('login')


@login_required
def user_profile(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST,instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,f"Your profile has been updated")
            return redirect('home')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    
    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request,"users/profile.html",context)
