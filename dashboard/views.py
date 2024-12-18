from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentForm
from .models import Student
from rest_framework.response import Response
from rest_framework import status
from .serializer import StudentSerializer,SUBJECTS
from rest_framework.decorators import api_view

# Create your views here.

@login_required(login_url='login')
def home(request): 
    return render(request,'dashboard/home.html', {"title":"home"})

@login_required
def dashboard(request):
    students = Student.objects.all()
    print(students)
    return render(request,"dashboard/dashboard.html",{'students': students})


@api_view(['GET'])
def student_data(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students,many=True)
    return Response(serializer.data)