from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from rest_framework.response import Response

# from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
#
#
# class CustomAuthToken(ObtainAuthToken):
#     serializer_class = UserSerializer
#     @swagger_auto_schema(request_body=AuthTokenSerializer, responses={200: UserSerializer()})
#     def post(self, request, *args, **kwargs) -> Response:
#         serializer = self.serializer_class(data=request.data, context=self.get_serializer_context())
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data["user"]
#         Token.objects.get_or_create(user=user)
#         user_serializer = UserSerializer(user)
#         return Response(user_serializer.data)
#
#
# class UserViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#
#
# # class RegistrationView(APIView):
# #     def post(self, request):
# #         serializer = UserSerializer(data=request.data)
# #         if serializer.is_valid():
# #             serializer.save()
# #             return Response(serializer.data, status=status.HTTP_201_CREATED)
# #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# # class LoginView(APIView):
# #     def post(self, request):
# #         if 'email' not in request.data or 'password' not in request.data:
# #             return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
# #         email = request.POST['email']
# #         password = request.POST['password']
# #         user = authenticate(request, email=email, password=password)
# #         if user is not None:
# #             login(request, user)
# #             auth_data = get_tokens_for_user(request.user)
# #             return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
# #         return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# serilaizer
from .serializers import UserSerializer
# from .serializers import UserLoginSerializer

#
# class UserLoginAPIView(GenericViewSet, CreateModelMixin):
#     def create(self, request, *args, **kargs):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             response = {
#                 "username": {
#                     "detail": "User Doesnot exist!"
#                 }
#             }
#             if User.objects.filter(username=request.data['username']).exists():
#                 user = User.objects.get(username=request.data['username'])
#                 token, created = Token.objects.get_or_create(user=user)
#                 response = {
#                     'success': True,
#                     'username': user.username,
#                     'email': user.email,
#                     'token': token.key
#                 }
#                 return Response(response, status=status.HTTP_200_OK)
#             return Response(response, status=status.HTTP_400_BAD_REQUEST)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class hueta(GenericViewSet, CreateModelMixin):
    serializer_class = UserSerializer

    def create(self, request, *args, **kargs):
        data = {}
        for key, item in request.data.items():
            data[key] = item
        a = User.objects.create_user(**data)
        response = {
            'success': True,
            'user': data,
            'token': Token.objects.create(user=a).key
        }
        return Response(response, status=status.HTTP_201_CREATED)


class UserLogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({"success": True, "detail": "Logged out!"}, status=status.HTTP_200_OK)
