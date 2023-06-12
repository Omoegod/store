from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.html import format_html

from catalog.models import House, FloorPlan, Location, Room, FloorPlanImage, HouseImage
# Register your models here.

class HouseImageInline(admin.StackedInline):
    model = HouseImage

class RoomInline(admin.StackedInline):
    model = Room

class LocationInline(admin.StackedInline):
    model = Location

class FloorPlanInline(admin.StackedInline):
    model = FloorPlan
    readonly_fields = ['edit_floor_plan']

    def edit_floor_plan(self, obj):
        if obj.pk:
            url = reverse('admin:catalog_floorplan_change', args=[obj.pk])
            return format_html('<a href="{}">Edit Floor Plan</a>', url)
        return ''
    
class FloorPlanImageInline(admin.StackedInline):
    model = FloorPlanImage    

class HouseAdmin(admin.ModelAdmin):
    inlines = [HouseImageInline, FloorPlanInline, LocationInline]
    
class FloorPlanAdmin(admin.ModelAdmin):
    inlines = [FloorPlanImageInline, RoomInline]
        
    def response_change(self, request, obj):
        if "_continue" in request.POST:
            return super().response_change(request, obj)
        else:
            url = reverse('admin:catalog_house_change', args=[obj.house.pk])
            return HttpResponseRedirect(url)

admin.site.register(House, HouseAdmin)
admin.site.register(FloorPlan, FloorPlanAdmin)
admin.site.register(Location)
admin.site.register(Room)