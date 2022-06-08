from django.db import models


# Create your models here.
class Hospital(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60, default="India")
    phone_number1 = models.IntegerField(null=True, blank=True)
    phone_number2 = models.IntegerField(null=True, blank=True)
    hospital_photo = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True,
                                       null=True)

    def __str__(self):
        return self.name


class HomeNurses(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    availability = models.BooleanField(default=True)
    home_nurse_photo = models.ImageField(upload_to=None, null=True, blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    specialisation = models.CharField(max_length=30, blank=True, null=True)
    online_mode = models.BooleanField(default=True)
    rating = models.FloatField(default=3)
    doctor_photo = models.ImageField(upload_to=None, null=True, blank=True)
    hospital = models.ForeignKey(Hospital, related_name="doctor", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class WorkingTime(models.Model):
    days = (
        (1, "monday"), (2, "tuesday"), (3, "Wednesday"), (4, "Thursday"), (5, "friday"), (6, "saturday"), (7, "sunday"))
    day = models.IntegerField(default=1, choices=days)
    starting_time = models.TimeField()
    ending_time = models.TimeField()

    def __str__(self):
        return self.day


class MedicalHistory(models.Model):
    date = models.DateField()
    record = models.TextField()
    prescription_photo = models.ImageField(upload_to=None, null=True, blank=True)

    def __str__(self):
        return self.date


class BloodDonation(models.Model):
    date = models.DateField()
    blood_bank_name = models.CharField(max_length=40)
    blood_bank_location = models.CharField(max_length=40)
    phone_number1 = models.IntegerField(null=True, blank=True)
    phone_number2 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.date


'''class PhysicalTherapy(models.Model):
    
    def __str__(self):
        return self.name'''
