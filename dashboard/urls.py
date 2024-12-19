from django.urls import path
from .views import home,dashboard,student_data,student_details,student_detail_view

urlpatterns = [
    path('',home,name='home'),
    path('dashboard/',dashboard,name="dashboard"),
    path('api/students/',student_data,name='student_data'),
    path('api/students/<int:pk>/',student_details,name='student_details'),
    path('students/<int:pk>/',student_detail_view,name="student_detail")
]