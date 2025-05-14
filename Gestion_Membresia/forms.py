from django import forms
from .models import membresia

class MembresiaForm(forms.ModelForm): 
    class Meta: 
        model = membresia 
        fields = ['__all__']
        label = {
                'tipo_membresia': 'Tipo de membresia',
                'precio': 'Precio de la membresia'
                }
