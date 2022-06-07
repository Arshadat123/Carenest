from django.db import models


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    ima_no = models.CharField(max_length=30, blank=True, null=True)
    hospital = models.ForeignKey(Hospital, related_name="doctor", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.hospital.name
