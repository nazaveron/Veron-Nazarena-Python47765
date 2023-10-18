from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class UsuarioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repita contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class Buscar_Form(forms.Form):
    pulsera1989 = forms.CharField(max_length=100, label='Buscar pulsera')


class UserEditForm(UserChangeForm):
    password = forms.CharField(
        label="Nueva contraseña",
        required=False,
        widget=forms.PasswordInput,
        help_text="Deja este campo en blanco si no deseas cambiar la contraseña.")

    class Meta:
        model = User
        fields = ["username", "email"]