from django.contrib import admin
from .models import Image, Categories, Image_Location

# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal =('Categories',)

admin.site.register(Image)
admin.site.register(Categories)
admin.site.register(Image_Location)