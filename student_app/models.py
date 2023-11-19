from django.db import models

# Create your models here.

class Std(models.Model):
    firstname=models.CharField(max_length=50)
    middlename=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    father=models.CharField(max_length=50)
    mother=models.CharField(max_length=50)
    d=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    age=models.IntegerField()
    mobile=models.BigIntegerField()
    amobile=models.BigIntegerField()
    add=models.CharField(max_length=200)
    state=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
