from django.contrib import admin

from .models import Region, Classification, Color, Producer, Wine

admin.site.register(Region)
admin.site.register(Classification)
admin.site.register(Color)
admin.site.register(Producer)
admin.site.register(Wine)
