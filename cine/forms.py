from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['nombre_comprador', 'correo_comprador', 'cantidad']

    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        if cantidad < 1 or cantidad > 10:
            raise forms.ValidationError("La cantidad de entradas debe estar entre 1 y 10.")
        return cantidad