from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Correo Electrónico'}))
    pais = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'País'}))
    ciudad = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ciudad'}))
    
    class Meta:
        model = Subscriber
        fields = ('nombre', 'email', 'pais', 'ciudad',)