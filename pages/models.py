from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render
# Create your models here.
class Professionals(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.first_name} {self.second_name}"

class Service(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    second_name= models.CharField(max_length=30)
    professional = models.ForeignKey(Professionals, on_delete=models.CASCADE)
    services = models.ManyToManyField(Service)
    date = models.DateTimeField()
    phone = models.CharField(max_length=11)
    
    def __str__(self):
        return f"{self.first_name} {self.second_name}"






