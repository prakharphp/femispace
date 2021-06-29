from rest_framework import serializers
from health.models import *


class MonthCycleSerializer(serializers.ModelSerializer):

    class Meta:
        model = MonthCycle
        fields = ("user", "date", "is_actual", "is_menstruation", "is_follicular", "is_ovulation", "is_luteal",
                  "is_pre_menstruation", "feeling", "feeling", "tag", "updated_at", "created_at")


class AverageCycleSerializer(serializers.ModelSerializer):

    class Meta:
        model = AverageCycle
        fields = ("user", "menstruation_days", "follicular_days", "proliferative_days",
                  "luteal_days", "secretory_days", "updated_at")