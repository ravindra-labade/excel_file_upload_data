import datetime

from django.db import models

# Create your models here.


class Product(models.Model):
    prod_id = models.IntegerField()
    name = models.CharField(max_length=50)
    price = models.FloatField(null=True)
    quantity = models.IntegerField()
    mf_date = models.DateField(auto_now=True)
    exp_date = models.DateField(auto_now=True)
    hsn_no = models.IntegerField()