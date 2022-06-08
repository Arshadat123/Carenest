from rest_framework import serializers
from .models import *


class GetHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ["id", "name"]


class GetDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id", "name", "specialisation", "working_day", "time_schedule", "online_mode", "ima_no", "rating"]


class GetHomeNursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeNurses
        fields = ["id", "name", "experience", "availability"]
