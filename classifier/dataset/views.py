from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Plant
from classifier.request_history.models import RequestHistory
from rest_framework.parsers import MultiPartParser
from .serializers import PlantSerializer
from rest_framework.permissions import IsAuthenticated


IMAGE_PROCESSOR = lambda x: {"label": 1}


class ClassifierView(APIView):
    parser_classes = (MultiPartParser,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        image = request.data.get("image")
        if not image:
            return Response({"message": "image field is ewquired"}, status.HTTP_400_BAD_REQUEST)

        response = IMAGE_PROCESSOR(image)
        label = response["label"]

        plant = Plant.objects.filter(dataset__is_active=True, label__value=label).first()
        RequestHistory.objects.create(user=request.user, image=image, response=plant.info)
        serializer = PlantSerializer(plant)
        return Response(serializer.data)
