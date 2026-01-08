from django import forms
from .models import Participantes

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participantes
        fields = ['nome', 'email', 'curso']