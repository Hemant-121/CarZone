from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width"40px" height= "40px" style="border-radius:50px" alt=""/>'.format(object.photo.url))

    thumbnail.short_description = "Photo"

    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_date')
    list_display_links = ('id','thumbnail', 'first_name')

    # For Search bar
    search_fields = ('id', 'designation', 'first_name', 'last_name')
    list_filter = ('designation',)



admin.site.register(Team, TeamAdmin)

