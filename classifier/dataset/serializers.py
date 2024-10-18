from rest_framework import serializers
from .models import Plant, PlantImage


class PromoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantImage
        fields = ("image", )


class BaseCityMenuItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="info.name", read_only=True)
    full_name = serializers.CharField(source="info.full_name", read_only=True)
    description = serializers.CharField(source="info.description", read_only=True)
    images = PromoImageSerializer(source="info.images", many=True, read_only=True)
    # images = serializers.ImageField(source="info.image", read_only=True)

    class Meta:
        model = Plant
        fields = ("name", "full_name", "description", "images", )
