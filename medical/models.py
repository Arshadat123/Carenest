from django.db import models

# Create your models here.

class Profile(models.Model):
    name   = models.CharField(max_length=50)
    age    = models.CharField(max_length=3, blank=True, null=True) 
    phone  = models.CharField(max_length=13, blank=True, null=True) 
    email  = models.CharField(max_length=40, blank=True, null=True) 
    blood  = models.CharField(max_length=2, blank=True, null=True)
    weight = models.CharField(max_length=3, blank=True, null=True)
    image = models.ImageField(upload_to="pic", null=True, blank=True)

    def __str__(self):
        return self.name


class Pharmasy(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100, blank=True, null=True)
    rating = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.name
