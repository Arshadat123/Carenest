from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("doctor", DoctorViewSet)
router.register("home_nurses", HomeNursesViewSet)
router.register("hospitals", HospitalViewSet)
urlpatterns = [
    path(r'', include(router.urls)),
]

