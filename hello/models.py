from django.db import models


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class Person(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    age = models.IntegerField()
