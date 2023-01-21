from rest_framework import serializers
from .models import Color,Truck,Accessories


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
        

class TruckSerliazer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'
        
class AccessoriesSerliazer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = '__all__'