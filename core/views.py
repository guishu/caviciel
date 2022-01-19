from rest_framework import viewsets

from core.models import Producer
from core.serializers import ProducerSerializer, ProducerListSerializer


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProducerListSerializer
        else:
            return ProducerSerializer


