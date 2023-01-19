from django.urls import path
from . import views

urlpatterns = [
    path('colors/', views.GetColors, name='allcolors')
]