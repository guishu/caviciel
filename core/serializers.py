from rest_framework import serializers

from core.models import Producer


class ProducerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"
