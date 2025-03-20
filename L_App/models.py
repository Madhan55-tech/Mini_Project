from django.db import models

# Create your models here.

class UserId(models.Model):
    U_Name=models.CharField(max_length=20)
    Email=models.EmailField(max_length=20)
    Password=models.CharField(max_length=20)

