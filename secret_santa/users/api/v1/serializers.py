from rest_framework import serializers
from users.models import User


class UserSignUpSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password1 = serializers.CharField()
    password2 = serializers.CharField()

    def validate_email(self, value):
        lower_email = value.lower()

        if User.objects.filter(email__iexact=lower_email).exists():
            raise serializers.ValidationError("Email already exist")

        return value

    def validate(self, data):
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Password not match")

        return data
