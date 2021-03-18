from django.contrib import admin
from .models import Car
from django.utils.html import format_html

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width"40px" height= "40px" style="border-radius:50px" alt=""/>'.format(object.car_photo.url))

    thumbnail.short_description = "Car Image"

    list_display = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style','fuel_type','is_featured')
    list_display_links = ('id','thumbnail', 'car_title')

    # For Search bar
    search_fields = ('id', 'car_title', 'model', 'year')
    list_filter = ('car_title',)

admin.site.register(Car, CarAdmin)