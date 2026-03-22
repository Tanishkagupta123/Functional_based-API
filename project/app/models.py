from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100,default='N/A')
    email = models.EmailField(unique=True)
    contact = models.CharField()
    gender = models.CharField(max_length=10,default='N/A')
    city = models.CharField(max_length=50,default='N/A')

    def __str__(self):
        return self.name