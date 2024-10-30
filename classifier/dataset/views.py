from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Plant
from classifier.request_history.models import RequestHistory
from rest_framework.parsers import MultiPartParser
from .serializers import PlantSerializer, UnrecognizedPlantSerializer
from rest_framework.permissions import IsAuthenticated
from classifier.dataset.models import Dataset


IMAGE_PROCESSOR = lambda x: {"label": 1, "probability": 0.8}


class ClassifierView(APIView):
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        image = request.data.get("image")
        if not image:
            return Response({"message": "image field is required"}, status.HTTP_400_BAD_REQUEST)

        response = IMAGE_PROCESSOR(image)
        current_dataset = Dataset.objects.filter(is_active=True).first()
        if response["probability"] < current_dataset.threshold:
            RequestHistory.objects.create(user=request.user, image=image, info=current_dataset.unrecognized_info,)
            serializer = UnrecognizedPlantSerializer(current_dataset)
            return Response(serializer.data)
        plant = Plant.objects.filter(dataset__is_active=True, label__value=response["label"]).first()
        RequestHistory.objects.create(user=request.user, image=image, info=plant.info, label=plant.label)
        serializer = PlantSerializer(plant)
        return Response(serializer.data)
