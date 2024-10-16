from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            # "id",
            "username",
            "inst",
            "email",
            "password"
        )
        extra_kwargs = {"password": {"write_only": True}}

#
#
# from rest_framework import serializers
# from django.contrib.auth.models import User
# from rest_framework.exceptions import ValidationError
# from rest_framework import status
# from rest_framework.authtoken.models import Token
#
#
# class UserLoginSerializer(serializers.ModelSerializer):
#     id = serializers.PrimaryKeyRelatedField(read_only=True)
#     username = serializers.CharField(read_only=True)
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ["id", "username", "password"]
#
#
# class UserRegisterSerializer(serializers.ModelSerializer):
#     # id = serializers.PrimaryKeyRelatedField(read_only=True)
#     # username = serializers.CharField()
#     # first_name = serializers.CharField()
#     # last_name = serializers.CharField()
#     # email = serializers.EmailField()
#     # password = serializers.CharField(write_only=True)
#     # password2 = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ["username", "email", "password"]
#         extra_kwargs = {
#             'password': {"write_only": True}
#         }
#
#     def validate_username(self, username):
#         if User.objects.filter(username=username).exists():
#             detail = {
#                 "detail": "User Already exist!"
#             }
#             raise ValidationError(detail=detail)
#         return username
#
#     def validate(self, instance):
#         if instance['password'] != instance['password2']:
#             raise ValidationError({"message": "Both password must match"})
#
#         if User.objects.filter(email=instance['email']).exists():
#             raise ValidationError({"message": "Email already taken!"})
#
#         return instance
#
#     def create(self, validated_data):
#         passowrd = validated_data.pop('password')
#         passowrd2 = validated_data.pop('password2')
#         user = User.objects.create(**validated_data)
#         user.set_password(passowrd)
#         user.save()
#         Token.objects.create(user=user)
#         return user
