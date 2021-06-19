from rest_framework import serializers
from users.models import User
from django.db import models


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'gender', 'tag')
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     password = validated_data.pop('password')
    #     user = User(**validated_data)
    #     user.set_password(password)
    #     user.save()
    #     return user