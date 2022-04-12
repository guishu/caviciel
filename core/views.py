from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Producer
from core.serializers import ProducerSerializer


class ProducerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer



