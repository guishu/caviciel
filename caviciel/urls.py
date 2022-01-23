from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from core.views import ProducerViewSet


ROOT_API_PATH = "rest/api/latest"

router = routers.DefaultRouter()
router.register(r'producers', ProducerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(f"{ROOT_API_PATH}/", include(router.urls)),
    path(f"{ROOT_API_PATH}/token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(f"{ROOT_API_PATH}/token/refresh", TokenRefreshView.as_view(), name="token_refresh")
]
