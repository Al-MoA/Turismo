from django import forms
from .models import Contacto, Regiones
class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class RegionForm(forms.ModelForm):

    class Meta:
        model = Regiones
        fields = '__all__'