from rest_framework import serializers
from .models import Color,Truck,Accessories,Collection


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
        
class CollectionsSerliazer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'