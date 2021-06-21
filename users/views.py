from django.shortcuts import render,HttpResponse
from users.serializers import UserSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from users.models import User
from . import serializers


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny, )


# def get_eating_habit(request):
#     user = request.POST.get('id')
#     date = request.POST.get('date',)
#     obj = User.objects.get(id=int(user))
#     tag = obj.tag