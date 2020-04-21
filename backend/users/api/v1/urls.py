from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HGgfhViewSet

router = DefaultRouter()
router.register("hggfh", HGgfhViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
