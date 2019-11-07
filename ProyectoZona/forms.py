from django import forms
from .models import Pintura, Actor


class PinturaForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Pintura
        fields = ('nombre', 'codigo', 'color')

    def __init__ (self, *args, **kwargs):
        super(PinturaForm, self).__init__(*args, **kwargs)
        self.fields["pintor"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["pintor"].help_text = "Ingrese los pintores"
        self.fields["pintor"].queryset = pintor.objects.all()
