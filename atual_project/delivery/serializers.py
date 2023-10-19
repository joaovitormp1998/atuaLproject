from rest_framework import serializers
from .models import DeliveryRoute

class DeliveryRouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryRoute
        fields = '__all__'
