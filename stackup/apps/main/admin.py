from django.contrib import admin

from stackup.apps.main.models import *

class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'crime_score')

admin.site.register(Region, RegionAdmin)
admin.site.register(StandardOfLiving)

