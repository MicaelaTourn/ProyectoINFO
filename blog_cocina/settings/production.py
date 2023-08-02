from .base import *
# SECURITY WARNING: don't run with debug turned on in production!


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blogcocina4$default',
        'USER': 'blogcocina4',
        'PASSWORD': 'comision6g4',
        'HOST': 'blogcocina4.mysql.pythonanywhere-services.com',
        'PORT': ''
    }
}