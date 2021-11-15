from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_img_url = models.ImageField()
    created_on = models.DateField()
    active = models.BooleanField() 
    