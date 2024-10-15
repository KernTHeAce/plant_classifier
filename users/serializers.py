
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """It returns user's auth_token. Don't use it in any cases except for user auth"""

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "inst",
            "email",
            "password"
        )
        extra_kwargs = {"password": {"write_only": True}}
