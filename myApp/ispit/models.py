from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    address = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name + self.surname


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    is_active = models.BooleanField( blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.IntegerField( primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user_created = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='data/', blank=True, null=True)
    price = models.FloatField( blank=True, null=True)
    quantity = models.IntegerField( blank=True, null=True)

    def __str__(self):
        return self.name


class Sale(models.Model):
    #products = models.ForeignKey(Product, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_sold = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.date_sold

class SaleProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
