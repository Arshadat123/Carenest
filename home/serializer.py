from rest_framework import serializers
from .models import Doctor, Hospital


class GetHospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ["id", "name"]


class GetDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ["id", "name", "ima_no"]
