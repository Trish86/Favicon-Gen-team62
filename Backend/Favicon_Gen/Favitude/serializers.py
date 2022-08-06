from django.shortcuts import render

from rest_framework import viewsets, serializers

from django.contrib.auth.models import User

MIN_LENGTH = 8

class UserSerializer(serializers.ModelSerializer):

    Password = serializers.Charfield(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages={
            "min_length": f"password must be linger than {MIN_LENGTH} characters."
        }
    )

    Confirm_Password= serializers.Charfield(
        write_only = True,
        min_length = MIN_LENGTH,
        error_messages={
            "min_length": f"password must be longer than {MIN_LENGTH} characters."
        }
    )

    class Meta:
        model= User
        fields = "__all__"

    def validate(self, data):
        if data["Password"] != data ["Confirm Password"]:
            raise serializers.ValidationError("Invalid password")
            return data

    def create(self, validated_data):
        user = User.objects.create(
            full_name=validated_data["full_name"],
            email=validated_data["Email Address"],
            username=validated_data["username"],
            )

        user . Set_password(validated_data["Password"])
        user.save

        return user

class UserviewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

            


