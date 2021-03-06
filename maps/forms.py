from django import forms

from .models import CHOICES, RISK_CHOICES, ParticipatoryMap, Neighborhood

MAP_CHOICES = [(m.id, m.name) for m in ParticipatoryMap.objects.all()]
N_CHOICES = [(n.id, n.name) for n in Neighborhood.objects.all()]

class FilterMapForm(forms.  Form):
    neighborhood = forms.MultipleChoiceField(
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        choices=N_CHOICES,
        label='Bairro',
    )
    maps = forms.MultipleChoiceField(
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        choices=MAP_CHOICES,
        label='Mapa',
    )
    kind = forms.MultipleChoiceField(
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        choices=CHOICES,
        label='Tipo',
    )
    risk_kind = forms.MultipleChoiceField(
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
        choices=RISK_CHOICES,
        label='Tipo de Risco',
    )
