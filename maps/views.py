from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.conf import settings
from django.urls import reverse

from .models import Point, ParticipatoryMap, Symbol
from .forms import FilterMapForm


class ParticipatoryMapDetailView(FormMixin, DetailView):
    model = ParticipatoryMap
    template_name = "home.html"
    form_class = FilterMapForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pmap = self.get_object()
        context['mapa'] = pmap
        context['map'] = pmap.neighborhood.location.coords

        points = Point.objects.filter(pmap=pmap)
        if self.kind:
            points = points.filter(symbol__kind=self.kind)
        if self.risk_kind:
            points = points.filter(symbol__risk_kind=self.risk_kind)

        context['points'] = [[p.symbol.name, p.location.coords[1], p.location.coords[0], p.id] for p in points]
        context['api_key'] = settings.MAP_WIDGETS['GOOGLE_MAP_API_KEY']
        context['symbols'] = [[s.name, s.icon.url] for s in Symbol.objects.all()]

        return context

    def form_valid(self, form):
        self.kind = form.cleaned_data['kind']
        self.risk_kind = form.cleaned_data['risk_kind']
        return self.render_to_response(self.get_context_data(form=form))


class ParticipatoryMapsListView(ListView):
    model = ParticipatoryMap
    template_name = 'pmap-list-view.html'
