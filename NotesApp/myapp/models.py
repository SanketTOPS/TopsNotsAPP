from django.db import models
from datetime import datetime

# Create your models here.

class userSignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class notes(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    option=models.CharField(max_length=100)
    files=models.FileField(upload_to="MyNotes")
    disc=models.TextField()

class contactus(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField()
    msg=models.TextField()
    
