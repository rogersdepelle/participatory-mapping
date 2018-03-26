from django.db import models
from django.contrib.gis.db import models as gis_models


class Neighborhood(models.Model):

    class Meta:
        verbose_name = "Bairro"
        verbose_name_plural = "Bairros"

    name = models.CharField(max_length=45,verbose_name='Nome')
    location = gis_models.PointField()

    def __str__(self):
        return self.name


class ParticipatoryMap(models.Model):

    class Meta:
        verbose_name = "Mapa Comunitário"
        verbose_name_plural = "Mapas Comunitários"

    name = models.CharField(max_length=45, verbose_name='Nome')
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.CASCADE,
        verbose_name='Bairro'
    )

    def __str__(self):
        return self.name


class Symbol(models.Model):

    class Meta:
        verbose_name = "Símbolo"
        verbose_name_plural = "Símbolos"

    name = models.CharField(max_length=45, verbose_name='Nome')
    code = models.IntegerField(verbose_name='Código')
    icon = models.ImageField(verbose_name='Ícone', blank=True, null=True)

    def __str__(self):
        return self.name


class Point(models.Model):

    class Meta:
        verbose_name = "Ponto"
        verbose_name_plural = "Pontos"

    pmap = models.ForeignKey(
        ParticipatoryMap,
        on_delete=models.CASCADE,
        verbose_name='Mapa'
    )
    symbol = models.ForeignKey(
        Symbol,
        on_delete=models.CASCADE,
        verbose_name='Símbolo'
    )

    location = gis_models.PointField()

    def __str__(self):
        return str(self.location)
