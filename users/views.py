from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet

from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User


class CustomAuthToken(ObtainAuthToken):
    @swagger_auto_schema(request_body=AuthTokenSerializer, responses={200: UserSerializer()})
    def post(self, request, *args, **kwargs) -> Response:
        serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        Token.objects.get_or_create(user=user)
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)


class UserViewSet(GenericViewSet, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
