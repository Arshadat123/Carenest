from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Hospital)
admin.site.register(models.Doctor)
admin.site.register(models.HomeNurses)
admin.site.register(models.WorkingTime)
admin.site.register(models.MedicalHistory)
admin.site.register(models.BloodDonation)
