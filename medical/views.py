from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions
from .serializer import GetPharmasySerializer
from .serializer import GetProfileSerializer
from .models import Pharmasy 
from .models import Profile


class PharmasyViewSet(viewsets.ModelViewSet):
    serializer_class = GetPharmasySerializer
    queryset = Pharmasy.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "post", "patch"]

class PharmasyViewSet(viewsets.ModelViewSet):
    serializer_class = GetProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "post", "patch"]

class LabViewSet(viewsets.ModelViewSet):
    serializer_class = GetProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "post", "patch"]
