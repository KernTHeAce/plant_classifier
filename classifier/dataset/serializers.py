from rest_framework import serializers
from .models import Plant, PlantImage


class PlantImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ("image", )


class PlantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="info.name", read_only=True)
    full_name = serializers.CharField(source="info.full_name", read_only=True)
    description = serializers.CharField(source="info.description", read_only=True)
    images = PlantImageSerializer(source="info.images", many=True, read_only=True)

    class Meta:
        model = Plant
        fields = ("name", "full_name", "description", "images", )
