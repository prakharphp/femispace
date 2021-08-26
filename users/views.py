from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from users.models import User
from . import serializers
from .forms import UserRegisterForm
from django.contrib import messages


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny, )


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            return render(request, 'login.html', {})
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {'form': form})