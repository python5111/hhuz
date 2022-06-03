from atexit import register
from pyexpat import model
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
    title=models.CharField(max_length=35)
    citiy=models.CharField(max_length=11, choices=CITIYS, default="Toshkent")
    salary=models.PositiveIntegerField()
    age=models.PositiveIntegerField()
    experience=models.PositiveIntegerField()
    phone=models.CharField(max_length=13)
    decription=models.TextField()
    register_date=models.DateTimeField(auto_now_add=True)

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
    full_name=models.CharField(max_length=35)
    genders=models.CharField(max_length=5,choices=GENDER, default="Erkak")
    citiy=models.CharField(max_length=11, choices=CITIYS, default="Toshkent")
    phone=models.CharField(max_length=13)
    birth_date=models.DateField()
    register_date=models.DateTimeField(auto_now_add=True)
    experience=models.PositiveIntegerField()
    salary=models.PositiveIntegerField()
    decription=models.TextField()
