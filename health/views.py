from django.shortcuts import render
from rest_framework import viewsets
from health.models import MonthCycle
from . import serializers
from rest_framework.permissions import AllowAny


class MonthCycleApiViewSet(viewsets.ModelViewSet):
    queryset = MonthCycle.objects.prefetch_related(
         "tag", "feeling"
    ).all()
    serializer_class = serializers.MonthCycleSerializer
    permission_classes = (AllowAny,)
