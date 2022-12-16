from django import forms
from .models import Contact
 
class ContactForm(forms.ModelForm):
    name = forms.CharField(label="Nombre y Apellido", required=True, widget=forms.TextInput(attrs={'id':'name-surname', 'class': 'input-style input'}))
    email = forms.EmailField(label="Direccion de correo electronico" ,required=True, widget=forms.EmailInput(attrs={'id':'email', 'class': 'input-style input'}))
    phone = forms.CharField(label="Telefono", required=True, widget=forms.TextInput(attrs={'id':'phone', 'class': 'input-style input'}))
    content = forms.CharField(label="Mensaje" ,required=True, widget=forms.Textarea(attrs={'id':'message', 'class': 'input-style textarea', 'cols':30,  'rows':10}))
    
    class Meta:
        model = Contact
        fields = '__all__'