from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import Student,SUBJECTS

# Create your views here.

@login_required(login_url='login')
def home(request): 
    return render(request,'dashboard/home.html', {"title":"home"})

@login_required
def dashboard(request):
    students = Student.objects.all()
    print(students)
    return render(request,"dashboard/dashboard.html",{'students': students})
