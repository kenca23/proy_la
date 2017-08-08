from django import forms

class ContactForm(forms.Form):
    CORREOS = (
        ('Kenneth Calvo', 'Kenneth Calvo'),
        ('Kevin Calvo', 'Kevin Calvo'),
    )
    nombre = forms.CharField(required=True, max_length=35)
    email = forms.EmailField(required=True)
    dirigido = forms.ChoiceField(choices=CORREOS, required=True)
    asunto = forms.CharField(required=True, max_length=35)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        max_length=600
    )