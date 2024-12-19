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

class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=20,choices=COURSES)

    def __str__(self):
        return self.name 

class StudentMarks(models.Model):
    student = models.ForeignKey('Student',on_delete=models.CASCADE,related_name='subject_marks')
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.name} : {self.score}"

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
    marks = models.IntegerField()
    bookmarked = models.BooleanField(default=False)

    def __str__(self):
        return self.name 
    
    def get_subjects(self):
        return SUBJECTS.get(self.course, [])
    
    def get_marks(self):
        subject_marks = StudentMarks.objects.filter(student=self)
        dict_marks = {subject_mark.subject.name: subject_mark.score for subject_mark in subject_marks}
        return dict_marks