from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PharmeasyViewSet

router = DefaultRouter()
router.register("pharmeasy", PharmeasyViewSet)
router.register("profile", PharmeasyViewSet)
urlpatterns = [
    path(r'', include(router.urls)),
]
