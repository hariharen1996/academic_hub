from django.shortcuts import render,redirect,get_object_or_404
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

@api_view(['GET'])
def student_details(request,pk):
    student = Student.objects.get(pk=pk)
    print(student)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

def student_detail_view(request,pk):
    student = get_object_or_404(Student,pk=pk)
    return render(request,"dashboard/student_details.html",{'student':student})