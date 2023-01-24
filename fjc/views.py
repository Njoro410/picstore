from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from fjc.models import User,Truck,Accessories,Collection,CollectionImage,Color
from .serializers import ColorSerializer,TruckSerializer,AccessoriesSerializer,CollectionsSerializer,CollectionsImagesSerializer

# Create your views here.
@api_view(['GET'])
def GetColors(request):
    colors = Color.objects.all()
    serializer = ColorSerializer(colors, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetTruck(request):
    trucks = Truck.objects.all()
    serializer = TruckSerializer(trucks, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def GetAccessories(request):
    acessories = Accessories.objects.all()
    serializer = AccessoriesSerializer(trucks, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetCollections(request):
    collections = Collection.objects.all()
    serializer = CollectionsSerializer(collections, many=True)
    return Response(serializer.data)

##gets single item from collection
@api_view(['GET'])
def GetCollection(request,id):
    collections = Collection.objects.get(id=id)
    serializer = CollectionsSerializer(collections, many=False)
    return Response(serializer.data)

##get collection images
@api_view(['GET'])
def GetCollectionImages(request,id):
    collections = CollectionImage.objects.filter(collection_id=id)
    serializer = CollectionsImagesSerializer(collections, many=True)
    return Response(serializer.data)