from rest_framework import serializers

from classifier.dataset.serializers import BaseCityMenuItemSerializer
from .models import RequestHistory


class RequestHistorySerializer(serializers.ModelSerializer):
    response = BaseCityMenuItemSerializer()

    class Meta:
        model = RequestHistory
        fields = "__all__"
