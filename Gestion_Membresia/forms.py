from django import forms
from .models import membresia

class MembresiaForm(forms.ModelForm):
    """
    Formulario basado para el modelo 'membresia'
    """ 
    class Meta: 
        model = membresia 
        """
        Especifica el modelo al que pertenece el formulario
        """
        fields = ['__all__']
        """
        Define qué campos del modelo deben incluirse en el formulario
        """
        label = {
                'tipo_membresia': 'Tipo de membresia',
                'precio': 'Precio de la membresia'
                }
        """
        Permite personalizar las etiquetas que se muestran para los campos del formulario
        """
