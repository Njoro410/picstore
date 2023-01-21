from rest_framework import serializers
from .models import Color,Truck


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
        

class TruckSerliazer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'