from tokenize import Number
from django.db import models

# Create your models here.
class Product(models.Model):
    #------------Customer Suppot -----------
    Name = models.CharField(max_length=30)
    Warhouse=models.CharField(max_length=30)
    Number=models.IntegerField()
    def __str__(self):
        return self.Name
class Product_1(models.Model):

    #------------Customer Suppot -----------

    Name = models.CharField(max_length=30)
    Warhouse=models.CharField(max_length=30)
    Qty=models.IntegerField()
    serial_num=models.IntegerField()
    color=models.CharField(max_length=30,blank=True,null=True)
    model_type=models.CharField(max_length=30,blank=True,null=True)
    capisty=models.CharField(max_length=30,blank=True, null=True)

    def __str__(self):
        return self.Name


