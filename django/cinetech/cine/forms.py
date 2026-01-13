from django import forms

class EspectadorForm(forms.Form):
    nome = forms.CharField(max_length=100)
    cpf = forms.CharField(max_length=11)
    meia = forms.BooleanField(required=False, 
                              label='meia entrada')
    

