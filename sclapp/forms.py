from django import forms
from django.forms import fields
from .models import Orgao

class CadOrgaoForm(forms.ModelForm):
    class Meta:
        model = Orgao

        fields = [
            'nome',
            'cidade',
            'uf'
        ]
        



