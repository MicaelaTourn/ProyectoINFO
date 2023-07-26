from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'tipo_usuario']
    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('imagen', 'tipo_usuario')}),
    )

admin.site.register(Usuario, UsuarioAdmin)