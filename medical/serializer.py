from rest_framework import serializers
from .models import Pharmeasy, Profile


class GetProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "name", "age", "email", "phone", "blood", "weight"]


class GetPharmeasySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmeasy 
        fields = ["id", "name", "rating", "location"]
