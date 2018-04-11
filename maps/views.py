from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.conf import settings

from .models import Point, ParticipatoryMap, Symbol

class ParticipatoryMapDetailView(DetailView):
    model = ParticipatoryMap
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pmap = self.get_object()
        points = Point.objects.filter(pmap=pmap)
        context['mapa'] = pmap
        context['map'] = pmap.neighborhood.location.coords
        context['points'] = [[p.symbol.name, p.location.coords[1], p.location.coords[0], p.id] for p in points]
        context['api_key'] = settings.MAP_WIDGETS['GOOGLE_MAP_API_KEY']
        context['symbols'] = [[s.name, s.icon.url] for s in Symbol.objects.all()]
        return context


class ParticipatoryMapsListView(ListView):
    model = ParticipatoryMap
    template_name = 'pmap-list-view.html'
