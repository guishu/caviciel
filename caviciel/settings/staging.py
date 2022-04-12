from .base import *
import dj_database_url

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS')]

DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

DEBUG = os.getenv('DEBUG') == "True"
