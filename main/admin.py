from django.contrib import admin

from .models import CollectionPlaces, MaterialType, Partners, User

# Register your models here.
admin.site.register(User)
admin.site.register(CollectionPlaces)
admin.site.register(MaterialType)
admin.site.register(Partners)
