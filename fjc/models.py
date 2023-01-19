from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

# Create your models here.
class Truck(models.Model):
    name = models.CharField(max_length=10, default='FJ Cruiser')
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='picsgalore/fj/truck/', blank=True)
    color = models.ForeignKey('Color', on_delete=models.DO_NOTHING)
    year = models.IntegerField(default=2014, blank=True )
    tags = TaggableManager()
    uploaded_By = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    upload_Date = models.DateTimeField(auto_now_add=True, null=True)
    accessories = models.ForeignKey('Accessories', on_delete=models.DO_NOTHING,null=True, blank=True)
    status = models.ForeignKey('Status', on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.name
    
    

class Accessories(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(max_length=50, blank=True, null=True)
    manufacturer = models.CharField(max_length=50, blank=True, null=True)
    uploaded_By = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='picsgalore/fj/accessories/', null=True)
    
    def __str__(self):
        return self.name
    
    
class Collection(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    uploaded_By = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    image = models.ImageField(null=True)
    tags = TaggableManager()
    
    def __str__(self):
        return self.title
    
    
class CollectionImage(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='picsgalore/fj/collection/', null=True)
    
    def __str__(self):
        return self.collection.title
    
class Color(models.Model):
    COLORS = (
        ("Iceberg", "Iceberg"),
        ("Black Diamond", "Black Diamond"),
        ("Black","Black"),
        ("Titanium", "Titanium"),
        ("Silver Fresco", "Silver Fresco"),
        ("Cement Gray", "Cement Gray"),
        ("Amy Green", "Amy Green"),
        ("Sandstorm", "Sandstorm"),
        ("Quicksand", "Quicksand"),
        ("Sun Fusion", "Sun Fusion"),
        ("Magma", "Magma"),
        ("Black Cherry", "Black Cherry"),
        ("Brick", "Brick"), 
        ("Voodoo Blue", "Voodoo Blue"),
        ("Cavalry Blue", "Cavalry Blue"),
        ("Radiant Red", "Radiant Red"),
    )
    

    name = models.CharField(max_length=50, blank=False, null=False, choices=COLORS)


    
    def __str__(self):
        return self.name
    
    
class Status(models.Model):
    OPTIONS = (
        ("active", "active"),
        ("inactive", "inactive"),
    )
    
    name = models.CharField(max_length=50, blank=False, null=False, choices=OPTIONS)

    def __str__(self):
        return self.name