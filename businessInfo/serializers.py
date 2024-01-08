from rest_framework import serializers
from .models import BusinessInfo


class BusinessInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessInfo
        fields = '__all__'
