from django import forms
from .models import Contacto, Regione
class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'

class RegionForm(forms.ModelForm):

    class Meta:
        model = Regione
        fields = '__all__'