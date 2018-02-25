from mapwidgets.widgets import GooglePointFieldWidget

from django.contrib import admin
from django.contrib.gis.db import models as gis_models

from .models import Neighborhood


class NeighborhoodAdmin(admin.ModelAdmin):
    formfield_overrides = {
        gis_models.PointField: {"widget": GooglePointFieldWidget}
    }

admin.site.register(Neighborhood, NeighborhoodAdmin)
