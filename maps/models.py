from django.db import models
from django.contrib.gis.db import models as gis_models
from django.urls import reverse


CHOICES = (
    (1, 'Capacidades/Infraestrutura'),
    (3, 'Ameaças/Vulnerabilidades'),
    (2, 'Elementos do SCO'),
)

RISK_CHOICES = (
    (1, 'Geológicos, Hidrológicos e Meteorológicos'),
    (2, 'Biológicos'),
    (3, 'Sociais'),
    (4, 'Tecnológicos'),
)

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
        verbose_name = "Autor do Mapa"
        verbose_name_plural = "Autores Mapa"

    name = models.CharField(max_length=45, verbose_name='Nome')
    elderies = models.PositiveIntegerField(default=0, verbose_name='Idosos')
    pregnant_womans = models.PositiveIntegerField(default=0, verbose_name='Mulheres grávidas')
    physically_incapacitated = models.PositiveIntegerField(default=0, 'Portadores de necessidades especiais')
    babies = models.PositiveIntegerField(default=0, 'Crianças de colo')
    youngs = models.PositiveIntegerField(default=0, 'Jovens')
    pets = models.PositiveIntegerField(default=0, 'Animais de estimação')
    animal = models.PositiveIntegerField(default=0, 'Animais de maior porte')
    neighborhood = models.ForeignKey(
        Neighborhood,
        on_delete=models.CASCADE,
        verbose_name='Autor do Mapa'
    )

    def get_absolute_url(self):
        return reverse('pmap_detail_view', kwargs={'pk':str(self.id)})

    def __str__(self):
        return self.name


class Symbol(models.Model):

    class Meta:
        verbose_name = "Símbolo"
        verbose_name_plural = "Símbolos"

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

    radius = models.PositiveIntegerField(default=0, verbose_name='Raio em metros', help_text='deixar 0 para desenhar apenas um ponto')
    location = gis_models.PointField()

    def __str__(self):
        return str(self.location)
