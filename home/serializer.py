from rest_framework import serializers
from .models import *
import datetime


class GetHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ["id", "name", "location", "phone_number1", "phone_number2", "hospital_photo"]


class GetDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id", "name", "specialisation", "online_mode",  "rating", "doctor_photo"]


class GetHomeNursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeNurses
        fields = ["id", "name", "experience", "availability", "home_nurse_photo"]


class GetWorkingTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingTime
        fields = ["id", "day", "starting_time", "ending_time"]


class GetMedicalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalHistory
        fields = ["id", "date", "record", "prescription_photo"]


class GetBloodDonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BloodDonation
        fields = ["id", "date", "blood_bank_name", "blood_bank_location", "phone_number1", "phone_number2"]
