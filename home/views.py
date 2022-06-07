from django.shortcuts import render


from rest_framework import viewsets, permissions
from .serializer import GetDoctorSerializer
from .models import Doctor


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = GetDoctorSerializer
    queryset = Doctor.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "post", "patch"]
