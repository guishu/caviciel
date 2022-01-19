from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from core.views import ProducerViewSet

router = routers.DefaultRouter()
router.register(r'producers', ProducerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
