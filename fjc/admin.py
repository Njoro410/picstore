from django.contrib import admin
from .models import Truck,Accessories,Color,Collection,CollectionImage,Status

# Register your models here.
admin.site.register(Truck)
admin.site.register(Accessories)
admin.site.register(Color)
admin.site.register(Status)

 
class CollectionImageAdmin(admin.StackedInline):
    model = CollectionImage
 
@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    inlines = [CollectionImageAdmin]
 
    class Meta:
       model = Collection
 
@admin.register(CollectionImage)
class CollectionImageAdmin(admin.ModelAdmin):
    pass