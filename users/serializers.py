from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


class UserSerializer(serializers.ModelSerializer):

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

    def validate(self, attrs):
        if self.instance is None and not attrs.get("inst") and not attrs.get("email"):
            raise ValidationError("Need point at least one: inst or email")
        return super().validate(attrs)
