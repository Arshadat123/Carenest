from rest_framework import serializers
from .models import Pharmasy, Profile, Lab


class GetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "name", "age", "email", "phone", "blood", "weight", "image"]


class GetPharmasySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmasy 
        fields = ["id", "name", "rating", "location"]

class GetLabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab 
        fields = ["id", "name", "weight", "blood", "labreport"]
