from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("doctor", DoctorViewSet)
router.register("home_nurses", HomeNursesViewSet)
router.register("hospitals", HospitalViewSet)
router.register("workingtime", WorkingTimeViewSet)
router.register("medical_history", MedicalHistoryViewSet)
router.register("blood_donation", BloodDonationViewSet)

urlpatterns = [
    path(r'', include(router.urls)),
]

