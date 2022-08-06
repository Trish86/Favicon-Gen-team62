from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response

from Favicon_Gen.Favitude import UserSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]