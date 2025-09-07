from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    phone=models.CharField(max_length=10,null=True)
    joined_date=models.DateField(default=datetime.utcnow)