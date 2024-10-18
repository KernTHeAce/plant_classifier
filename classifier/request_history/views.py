from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from .serializers import RequestHistorySerializer
from .models import RequestHistory
from rest_framework.permissions import IsAuthenticated


class RequestHistoryViewSet(GenericViewSet, ListModelMixin):
    serializer_class = RequestHistorySerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        return RequestHistory.objects.filter(user=user)







