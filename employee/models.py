from django.db import models
from accounts.models import User
# Create your models here.


class Employee_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='profile_default.jpg', upload_to='profile_images')

    def __str__(self):
        return self.user.username
