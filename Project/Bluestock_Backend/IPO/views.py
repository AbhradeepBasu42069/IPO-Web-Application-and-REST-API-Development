from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import IPOInfo
from .serializers import IPOInfoSerializer

class IPOInfoViewSet(viewsets.ModelViewSet):
    queryset = IPOInfo.objects.all()
    serializer_class = IPOInfoSerializer

    
    