from django.db import models

# Create your models here.
class User(models.Model):
    Student_name = models.CharField(max_length=70)
    Teacher_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=100)
