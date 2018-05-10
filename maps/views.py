from django.shortcuts import render
from django.views.generic.edit import FormView
from django.conf import settings
from django.urls import reverse

from .models import Neighborhood, Point, Symbol
from .forms import FilterMapForm


class HomeView(FormView):
    template_name = "home.html"
    form_class = FilterMapForm
    kinds = None
    risk_kinds = None
    maps = None
    neighborhoods = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        points = Point.objects.all()

        if self.neighborhoods:
            points = points.filter(pmap__neighborhood__in=self.neighborhoods)
        if self.maps:
            points = points.filter(pmap__in=self.maps)
        if self.kinds:
            points = points.filter(symbol__kind__in=self.kinds)
        if self.risk_kinds:
            points = points.filter(symbol__risk_kind__in=self.risk_kinds)

        context['points'] = [[p.symbol.name, p.location.coords[1], p.location.coords[0], p.id] for p in points]
        context['api_key'] = settings.MAP_WIDGETS['GOOGLE_MAP_API_KEY']
        context['symbols'] = [[s.name, s.icon.url] for s in Symbol.objects.all()]

        return context

    def form_valid(self, form):
        self.kinds = form.cleaned_data['kind']
        self.risk_kinds = form.cleaned_data['risk_kind']
        self.maps = form.cleaned_data['maps']
        self.neighborhoods = form.cleaned_data['neighborhood']
        return self.render_to_response(self.get_context_data(form=form))
