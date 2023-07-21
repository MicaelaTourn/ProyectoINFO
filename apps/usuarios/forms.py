from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    email = forms.EmailField(label='Correo', required=True)
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellido', required=True)
    password1 = forms.CharField(
        label='Contraseña', widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(
        label='Confirmar Contraseña', widget=forms.PasswordInput, required=True)
    
    """ Tipo de usuario """
    TIPOS_USUARIO_CHOICES = (('publico', 'Público'),('colaborador', 'Colaborador'),)
    tipo_usuario = forms.ChoiceField(label='Tipo de Usuario',choices=TIPOS_USUARIO_CHOICES,widget=forms.RadioSelect,required=True, )


    class Meta:
        model = Usuario
        fields = [
            'first_name',
            'last_name',
            'tipo_usuario',
            'username',
            'email',
            'password1',
            'password2'
        ]