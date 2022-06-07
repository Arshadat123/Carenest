from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions
from .serializer import GetPharmeasySerializer
from .serializer import GetProfileSerializer
from .models import Pharmeasy 
from .models import Profile


class PharmeasyViewSet(viewsets.ModelViewSet):
    serializer_class = GetPharmeasySerializer
    queryset = Pharmeasy.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "post", "patch"]

class PharmeasyViewSet(viewsets.ModelViewSet):
    serializer_class = GetProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [permissions.AllowAny]
    http_method_names = ["get", "post", "patch"]
