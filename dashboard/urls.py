from django.urls import path
from .views import home,dashboard,student_data

urlpatterns = [
    path('',home,name='home'),
    path('dashboard/',dashboard,name="dashboard"),
    path('api/students/',student_data,name='student_data')
]