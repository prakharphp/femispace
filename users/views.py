from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from users.models import User
from . import serializers


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny, )
