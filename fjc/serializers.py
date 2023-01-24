from rest_framework import serializers
from .models import Color,Truck,Accessories,Collection,CollectionImage


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'
        

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = '__all__'
        
class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = '__all__'
        
class CollectionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'
        

class CollectionsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectionImage
        fields = '__all__'