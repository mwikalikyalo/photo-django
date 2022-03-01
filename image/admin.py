from django.contrib import admin
from .models import Category, Image, Location

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
# Register your models here.
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Location)