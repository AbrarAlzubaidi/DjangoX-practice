from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Auther(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    location = models.TextField()

    def __str__(self):
         return self.name

    def get_absolute_url(self):
         return reverse('auther_list')
         
class Book(models.Model):
    title = models.CharField(max_length= 200)
    description = models.TextField()
    auther = models.ForeignKey(Auther, on_delete= models.CASCADE) 
    rate = models.FloatField()

    def __str__(self):
         return self.title

    def get_absolute_url(self):
         return reverse('book_list')


