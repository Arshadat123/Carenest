from django.db import models


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100,blank=True,null= True)

    def __str__(self):
        return self.name


class HomeNurses(models.Model):
    name = models.CharField(max_length=30,blank=True,null=True)
    experience = models.IntegerField(blank=True,null=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    specialisation = models.CharField(max_length=30, blank=True, null=True)
    working_day = models.CharField(max_length=30, default="Mon-Fri")
    time_schedule = models.CharField(max_length=30, blank=True, null=True)
    online_mode = models.BooleanField(default=True)
    ima_no = models.CharField(max_length=30, blank=True, null=True)
    rating = models.FloatField(default=3)
    #hospital = models.ForeignKey(Hospital, related_name="doctor", on_delete=models.SET_NULL, null=True, blank=True)

    #def __str__(self):
        #return self.name + " " + self.hospital.name
