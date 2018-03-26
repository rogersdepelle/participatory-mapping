from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Point, ParticipatoryMap

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        points = Point.objects.all()
        context['map'] = ParticipatoryMap.objects.all()[0].neighborhood.location.coords
        context['points'] = [[p.symbol.name, p.location.coords[1], p.location.coords[0], p.id] for p in points]
        return context
