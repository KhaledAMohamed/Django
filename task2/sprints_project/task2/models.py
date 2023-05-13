from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    phone = models.IntegerField()
    address = models.CharField(max_length=400)

class Courses(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.CharField(max_length=500)
    course_duration = models.CharField(max_length=50)
    course_number = models.IntegerField()
