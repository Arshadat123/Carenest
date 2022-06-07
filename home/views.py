from django.shortcuts import render

from rest_framework import viewsets, permissions
from .serializer import GetDoctorSerializer, GetHomeNursesSerializer, GetHospitalSerializer
from .models import Doctor, HomeNurses, Hospital


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = GetDoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post", "patch"]


class HospitalViewSet(viewsets.ModelViewSet):
    serializer_class = GetHospitalSerializer
    queryset = Hospital.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post", "patch"]


class HomeNursesViewSet(viewsets.ModelViewSet):
    serializer_class = GetHomeNursesSerializer
    queryset = HomeNurses.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post", "patch"]
