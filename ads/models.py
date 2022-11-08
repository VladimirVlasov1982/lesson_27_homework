from django.db import models


# Create your models here.


class Ads(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    address = models.CharField(max_length=100)
    is_published = models.BooleanField()


class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
