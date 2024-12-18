from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    user_image = models.ImageField(default="default.jpg",upload_to="profilepic")

    def __str__(self):
        return f"{self.user.username} profile" 
    