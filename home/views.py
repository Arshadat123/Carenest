from django.shortcuts import render

from rest_framework import viewsets, permissions
from .serializer import *
from .models import *


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


class MedicalHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = GetMedicalHistorySerializer
    queryset = MedicalHistory.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post", "patch"]


class BloodDonationViewSet(viewsets.ModelViewSet):
    serializer_class = GetBloodDonationSerializer
    queryset = BloodDonation.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post", "patch"]


class WorkingTimeViewSet(viewsets.ModelViewSet):
    serializer_class = GetWorkingTimeSerializer
    queryset = WorkingTime.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    http_method_names = ["get", "post", "patch"]