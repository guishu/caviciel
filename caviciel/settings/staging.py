from .base import *

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS')]

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'caviciel',
            'USER': os.getenv('PG_USER'),
            'PASSWORD': os.getenv('PG_PASSWORD'),
            'HOST': os.getenv('PG_HOST'),
            'PORT': os.getenv('PG_PORT')
        }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
