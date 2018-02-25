from django.db import models
from django.contrib.gis.db import models as gis_models


class Neighborhood(models.Model):

    class Meta:
        verbose_name = "Neighborhood"
        verbose_name_plural = "Neighborhoods"

    name = models.CharField(max_length=100)
    point = gis_models.PointField()

    def __str__(self):
        return self.name

