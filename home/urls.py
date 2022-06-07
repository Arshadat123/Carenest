from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import DoctorViewSet

router = DefaultRouter()
router.register("doctor", DoctorViewSet)
urlpatterns = [
    path(r'', include(router.urls)),
]
