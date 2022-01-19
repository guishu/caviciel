from rest_framework import serializers

from core.models import Producer


class ProducerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ["id"]


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = "__all__"
