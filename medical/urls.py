from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PharmasyViewSet

router = DefaultRouter()
router.register("pharmeasy", PharmasyViewSet)
router.register("profile", PharmasyViewSet)
urlpatterns = [
    path(r'', include(router.urls)),
]
