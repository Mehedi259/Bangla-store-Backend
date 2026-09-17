from django.db import models

class Category(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50)
    image = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.CharField(max_length=50, null=True, blank=True)
    image = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    isBestSeller = models.BooleanField(default=False)
    
    stock = models.IntegerField(default=100)
    status = models.CharField(max_length=50, default="Active")

    def __str__(self):
        return self.name
