from rest_framework import serializers

from classifier.dataset.serializers import PlantSerializer
from .models import RequestHistory


class RequestHistorySerializer(serializers.ModelSerializer):
    response = PlantSerializer()

    class Meta:
        model = RequestHistory
        fields = "__all__"
