from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length= 200)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')