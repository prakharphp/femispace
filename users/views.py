from django.shortcuts import render,HttpResponse
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.serializers import UserSerializer
from . import serializers


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny, )

