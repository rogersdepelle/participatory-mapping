from django import forms

from .models import CHOICES, RISK_CHOICES

CHOICES = [(None, 'Selecione')] + list(CHOICES)
RISK_CHOICES = [(None, 'Selecione')] + list(RISK_CHOICES)

class FilterMapForm(forms.  Form):
    kind = forms.ChoiceField(choices=CHOICES, label='Tipo', required=False)
    risk_kind = forms.ChoiceField(choices=RISK_CHOICES, label='Tipo de Risco', required=False)
