from django.db import models

COURSES = [
    ('computer_science','Computer Science'),
    ('biology', 'Biology'),
    ('commerce', 'Commerce'),
    ('ai', 'Artificial Intelligence'),
]

SUBJECTS = {
    'computer_science': ['Physics','Chemistry','Maths','Computer Science','DSA'],
    'biology': ['Botany','Zoology','Physics','Chemistry','Maths'],
    'commerce': ['Accounts','Marketing','Commerce','Maths'],
    'ai': ['Python','Computer Science','Machine Learning',"Physics"]
}

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    roll_no = models.CharField(max_length=10,unique=True)
    course = models.CharField(max_length=20,choices=COURSES)
    student_image = models.ImageField(default="default_pic.jpg",upload_to='student_image',null=True,blank=True)
    email = models.EmailField()
    address = models.TextField()
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)
    marks = models.JSONField()
    bookmarked = models.BooleanField(default=False)

    def __str__(self):
        return self.name 
    
    def get_subjects(self):
        return SUBJECTS.get(self.course, [])
    
    