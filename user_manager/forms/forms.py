from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
        labels = {
            'username': 'Correo electrónico',
            'fist_name': 'Nombres',
            'last_name': 'Apellidos'
        }
        widgets = {
            'username': forms.EmailInput(attrs={'placeholder': 'Ej: example@domain.com'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Ej: María Angélica'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ej: Badillo Guerra'}),
        }

        help_texts = {
            'username' : 'Ingrese su correo electrónico . Debe contener letras, números y @.'
        }