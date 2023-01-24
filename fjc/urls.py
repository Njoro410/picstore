from django.urls import path
from . import views

urlpatterns = [
    path('colors/', views.GetColors, name='allcolors'),
    path('trucks/', views.GetTruck, name='alltruck'),
    path('accessories/', views.GetAccessories, name='allaccessories'),
    path('collections/', views.GetCollections, name='allcollections'),
    path('collectionimages/<str:id>/', views.GetCollectionImages, name='collectionimages')
]