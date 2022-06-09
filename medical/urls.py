from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register("pharmeasy", PharmasyViewSet)
router.register("lab", LabViewSet)
router.register("profile", ProfileViewSet)
urlpatterns = [
    path(r'', include(router.urls)),
]
