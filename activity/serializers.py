from rest_framework import serializers
from activity.models import EatRainbowActivity


class EatActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = EatRainbowActivity
        fields = ("user", "date", "is_actual", "red_serving", "cream_serving", "yellow_serving", "kiwi_serving",
                  "blue_serving",
                  "green_serving", "enjoy_regular", "eat_more", "eat_less", "eat_avoid", "tag", "comment")