from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IPOInfoViewSet

router = DefaultRouter()
router.register(r'ipo', IPOInfoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
