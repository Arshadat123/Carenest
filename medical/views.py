from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions, filters
from .serializer import GetPharmasySerializer, GetLabSerializer
from .serializer import GetProfileSerializer
from .models import Pharmasy
from .models import Profile


class PharmasyViewSet(viewsets.ModelViewSet):
    serializer_class = GetLabSerializer
    queryset = Pharmasy.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "post", "patch"]
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['name']



class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = GetProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "post", "patch"]


class LabViewSet(viewsets.ModelViewSet):
    serializer_class = GetProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "post", "patch"]
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['name']

