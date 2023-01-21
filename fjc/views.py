from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fjc.models import User,Truck,Accessories,Collection,CollectionImage,Color
from .serializers import ColorSerializer,TruckSerliazer,AccessoriesSerializer

# Create your views here.
@api_view(['GET'])
def GetColors(request):
    colors = Color.objects.all()
    serializer = ColorSerializer(colors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetTruck(request):
    trucks = Truck.objects.all()
    serializer = TruckSerliazer(trucks, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def GetAccessories(request):
    acessories = Accessories.objects.all()
    serializer = AccessoriesSerliazer(trucks, many=True)
    return Response(serializer.data)