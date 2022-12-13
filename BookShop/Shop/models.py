from django.db import models

# Create your models here.
class Product(models.Model):
    Image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    cost = models.IntegerField()

class Chosen_Product(models.Model):
    
    Image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    cost = models.IntegerField()
