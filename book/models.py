from django.db import models

# Create your models here.
class Book(models.Model):
    bid=models.AutoField(primary_key=True)
    titile=models.CharField(max_length=100)
    