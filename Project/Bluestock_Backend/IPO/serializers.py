from rest_framework import serializers
from .models import IPOInfo

class IPOInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPOInfo
        fields = '__all__'
