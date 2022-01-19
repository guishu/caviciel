from rest_framework import viewsets

from core.models import Producer
from core.serializers import ProducerSerializer


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
