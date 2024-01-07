from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    CategoryName=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    CategoryImage=models.ImageField(upload_to="Categories",null=True,blank=True)

class ProductDb(models.Model):
    Category_Name=models.CharField(max_length=100,null=True,blank=True)
    ProductName=models.CharField(max_length=100,null=True,blank=True)
    Description=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    ProductImage=models.ImageField(upload_to="product image",null=True,blank=True)