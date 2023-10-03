from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Category(models.Model):
    name=models.CharField(max_length=500)
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=10000)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.name  
    
class Product(models.Model):
    name= models.CharField(max_length=1000)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=10000)
    def __str__(self):
        return self.name   
class Place(models.Model):
    name= models.CharField(max_length=1000)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    def __str__(self):
        return self.name 
    


class Electronic_Review(models.Model):
    name = models.CharField(max_length=1000)
    mail = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.FloatField(default=5.0)
    review = models.TextField(max_length=10000)
    image = models.ImageField(upload_to='reviews/',blank=True,null=True)
    def __str__(self):
        return self.brand.name + ' Review by ' + self.name 

class Place_Review(models.Model):
    name = models.CharField(max_length=1000)
    mail = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    rating = models.FloatField(default=5.0)
    review = models.TextField(max_length=10000)
    image = models.ImageField(upload_to="reviews/",blank=True,null=True)
    def __str__(self):
        return self.place.name + ' Review by ' + self.name 