from rest_framework import serializers

from classifier.dataset.serializers import PlantImageSerializer, LabelSerializer
from .models import RequestHistory


class RequestHistorySerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="info.name", read_only=True)
    full_name = serializers.CharField(source="info.full_name", read_only=True)
    description = serializers.CharField(source="info.description", read_only=True)
    info_images = PlantImageSerializer(source="info.images", many=True, read_only=True)
    label = LabelSerializer()

    class Meta:
        model = RequestHistory
        fields = ("name", "full_name", "description", "label", "image", "info_images", )
