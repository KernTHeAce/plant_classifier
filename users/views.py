from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import get_object_or_404
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(GenericViewSet, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return get_object_or_404(self.get_queryset(), id=self.request.user.id)

    def get_permissions(self):
        if self.action == "create":
            return ()
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.validated_data["password"] = make_password(serializer.validated_data["password"])
        super().perform_create(serializer)

    def read_me(self, request):
        return self.retrieve(request)

    def update_me(self, request):
        return self.update(request)

    def partial_update_me(self, request):
        return self.partial_update(request)

    def destroy_me(self, request):
        return self.destroy(request)
