from mapwidgets.widgets import GooglePointFieldWidget

from django.contrib import admin
from django.contrib.gis.db import models as gis_models

from .models import Neighborhood, ParticipatoryMap, Point, Symbol


class NeighborhoodAdmin(admin.ModelAdmin):
    formfield_overrides = {
        gis_models.PointField: {"widget": GooglePointFieldWidget}
    }

class PointAdmin(admin.ModelAdmin):
    formfield_overrides = {
        gis_models.PointField: {"widget": GooglePointFieldWidget}
    }

admin.site.register(Neighborhood, NeighborhoodAdmin)
admin.site.register(ParticipatoryMap)
admin.site.register(Point, PointAdmin)
admin.site.register(Symbol)
