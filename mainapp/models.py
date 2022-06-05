from atexit import register
from pyexpat import model
from turtle import title
from django.db import models

# Create your models here.

class Job_creat(models.Model):
    CITIYS= [
        ("Toshkent","Toshkent"),
        ("Buxoro","Buxoro"),
        ("Farg'ona","Farg'ona"),
        ("Samarqand","Samarqand"),
        ("Andijon","Andijon"),
        ("Surxondaryo","Surxondaryo")
    ]
    STATUS=[
        ("active", "active"),
        ("passive","passive")
    ]
    job_title=models.CharField(max_length=35)
    citiy=models.CharField(max_length=11, choices=CITIYS, default="Toshkent")
    salary_min=models.PositiveIntegerField(null=True,blank=True)
    salary_max=models.PositiveIntegerField(null=True,blank=True)
    age=models.CharField(max_length=25,null=True)
    experience=models.CharField(max_length=155,null = True)
    phone=models.CharField(max_length=13)
    decription=models.TextField()
    register_date=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=8,choices=STATUS,default="active")
    photo = models.ImageField(upload_to = 'media/',null = True,blank = True)
    
    
    def __str__(self):
        return self.job_title

class Resume(models.Model):
    GENDER = [
        ("Erkak","Erkak"),
        ("Ayol","Ayol")

    ]
    CITIYS= [
        ("Toshkent","Toshkent"),
        ("Buxoro","Buxoro"),
        ("Farg'ona","Farg'ona"),
        ("Samarqand","Samarqand"),
        ("Andijon","Andijon"),
        ("Surxondaryo","Surxondaryo")
    ]
    full_name=models.CharField(max_length=85)
    genders=models.CharField(max_length=5,choices=GENDER, default="Erkak")
    citiy=models.CharField(max_length=11, choices=CITIYS, default="Toshkent")
    phone=models.CharField(max_length=13)
    birth_date=models.DateField(null=True)
    register_date=models.DateTimeField(auto_now_add=True)
    experience=models.PositiveIntegerField(null = True)
    salary=models.PositiveIntegerField(null = True)
    decription=models.TextField()
    
    def __str__(self):
        return self.full_name


class Blog(models.Model):
    title = models.CharField(max_length=55)
    photo = models.ImageField(upload_to="media")
    author = models.CharField(max_length=88)
    description = models.TextField()
    added_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    