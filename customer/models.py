from django.db import models

# Create your models here.

class Customer(models.Model):
    FirstName = models.CharField(max_length=30, verbose_name='Family Name')
    SecondName = models.CharField(max_length=30, verbose_name='Name')
    Email = models.EmailField(max_length=254)
    
    


