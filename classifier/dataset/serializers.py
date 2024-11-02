from rest_framework import serializers
from .models import Plant, PlantImage, Dataset, Label


class PlantImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = PlantImage
        fields = ("image", )

    def get_image(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.image.url)


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = "__all__"


class PlantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="info.name", read_only=True)
    full_name = serializers.CharField(source="info.full_name", read_only=True)
    description = serializers.CharField(source="info.description", read_only=True)
    images = PlantImageSerializer(source="info.images", many=True, read_only=True)

    class Meta:
        model = Plant
        fields = ("name", "full_name", "description", "images", )
       
        
class UnrecognizedPlantSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="unrecognized_info.name", read_only=True)
    full_name = serializers.CharField(source="unrecognized_info.full_name", read_only=True)
    description = serializers.CharField(source="unrecognized_info.description", read_only=True)
    images = PlantImageSerializer(source="unrecognized_info.images", many=True, read_only=True)

    class Meta:
        model = Dataset
        fields = ("name", "full_name", "description", "images", )
