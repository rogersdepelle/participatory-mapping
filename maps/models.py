from django.db import models
from django.contrib.gis.db import models as gis_models
from django.urls import reverse


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
    elderies = models.IntegerField(default=0)
    pregnant_womans = models.IntegerField(default=0)
    physically_incapacitated = models.IntegerField(default=0)
    babies = models.IntegerField(default=0)
    youngs = models.IntegerField(default=0)
    pets = models.IntegerField(default=0)
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.CASCADE,
        verbose_name='Bairro'
    )

    def get_absolute_url(self):
        return reverse('pmap_detail_view', kwargs={'pk':str(self.id)})

    def __str__(self):
        return self.name


class Symbol(models.Model):

    class Meta:
        verbose_name = "Símbolo"
        verbose_name_plural = "Símbolos"

    CHOICES = (
        (1, 'Infraestrutura'),
        (2, 'SCO'),
        (3, 'Riscos da Comunidade'),
    )

    RISK_CHOICES = (
        (1, 'Geológicos, Hidrológicos e Meteorológicos'),
        (2, 'Biológicos'),
        (3, 'Sociais'),
        (4, 'Tecnológicos'),
    )

    name = models.CharField(max_length=45, verbose_name='Nome')
    kind = models.IntegerField(verbose_name='Tipo', choices=CHOICES, blank=True, null=True)
    risk_kind = models.IntegerField(verbose_name='Tipo', choices=RISK_CHOICES, blank=True, null=True)
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
