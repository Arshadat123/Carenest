from rest_framework import serializers
from .models import Pharmasy, Profile


class GetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "name", "age", "email", "phone", "blood", "weight", "image"]


class GetPharmasySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmasy 
        fields = ["id", "name", "rating", "location"]
