import datetime
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . import serializers
from activity.models import EatRainbowActivity
from master.models import EatRainbowMaster
from users.models import User
from .utils import get_previous_date, get_difference_from_current_date, user_first_login
from datetime import date

# Eat Rainbow Activity


class EatActivityApiViewSet(viewsets.ModelViewSet):
    queryset = EatRainbowActivity.objects.prefetch_related(
         "enjoy_regular", "eat_more", "eat_less", "eat_avoid", "tag",
    ).all()
    serializer_class = serializers.EatActivitySerializer
    permission_classes = (AllowAny,)

    @action(
        detail=False,
        methods=['GET'],
        url_path=r"eat-rainbow-details",
        serializer_class=serializers.EatActivitySerializer
    )
    def get_eating_habit_by_date(self, request):
        """
        1. Need users tag
        2. match those with eatMaster data to get a query set
        3. match order with activity users previous date


        if previous date not exist
        eat     rainbow object filter by user and its last element
        eat rainbow object.master.sequence

        :param request:
        :return:
        """
        user = request.query_params.get('user_id')
        date = request.query_params.get('date')
        eat_rainbow_object = EatRainbowActivity.objects.filter(date=date, user=user)

        if not eat_rainbow_object:
            prev_date = get_previous_date(date)
            user_object = User.objects.get(id=user)
            previous_object_data = EatRainbowActivity.objects.filter(date=prev_date, user=user)
            user_tag = user_object.tag.filter().values_list('id', flat=True)
            eat_masters = EatRainbowMaster.objects.filter(tag__id__in=user_tag).distinct().order_by("sequence")
            # todo handle previous date not exist
            if not previous_object_data:
                previous_object_data = EatRainbowActivity.objects.filter(user=user).order_by("date")
                previous_date = previous_object_data.date
                previous_date_object = datetime.strptime(previous_date, "%Y-%m-%d")
                previous_sequence = previous_object_data.last().master.sequence
                diffrence_current_date = get_difference_from_current_date(previous_date_object)
                eat_rainbow_master_object = eat_masters.filter(sequence=(previous_sequence + diffrence_current_date)).first()
            else:
                previous_sequence = previous_object_data.first().master.sequence
                eat_rainbow_master_object = eat_masters.filter(sequence=(previous_sequence+1)).first()
            if not eat_rainbow_master_object:
                eat_rainbow_master_object = eat_masters.first()

            eat_rainbow_object, created = EatRainbowActivity.objects.update_or_create(user=user_object, date=date, defaults={'master':eat_rainbow_master_object,'red_serving': eat_rainbow_master_object.red_serving,
                                                          'cream_serving':eat_rainbow_master_object.cream_serving, 'yellow_serving': eat_rainbow_master_object.yellow_serving,
                                                          'kiwi_serving': eat_rainbow_master_object.kiwi_serving, 'blue_serving': eat_rainbow_master_object.blue_serving,
                                                          'green_serving':  eat_rainbow_master_object.green_serving})

            eat_rainbow_object.enjoy_regular.set(eat_rainbow_master_object.enjoy_regular.all(), clear=True)
            eat_rainbow_object.eat_more.set(eat_rainbow_master_object.eat_more.all(), clear=True)
            eat_rainbow_object.eat_less.set(eat_rainbow_master_object.eat_less.all(), clear=True)
            eat_rainbow_object.eat_avoid.set(eat_rainbow_master_object.eat_avoid.all(), clear=True)
            eat_rainbow_object.tag.set(eat_rainbow_master_object.tag.all(), clear=True)
            eat_rainbow_object.save()
        else:
            eat_rainbow_object = eat_rainbow_object.first()

        serializer = self.serializer_class(eat_rainbow_object).data if eat_rainbow_object else {}

        response_data = {
            "user": user,
            "date": date,
            "eat_rainbow_object": serializer
        }

        return Response(response_data)


def eat_rainbow(request):
    user = request.user
    use_id = user.id
    if request.POST.get('eat_date'):
        eat_date = request.POST.get('eat_date')
    else:
        eat_date = date.today()
        eat_date = eat_date.strftime("%Y-%m-%d")
    user_object = EatRainbowActivity.objects.filter(user=user)
    if not user_object:
        eat_rainbow_object = user_first_login(user, eat_date)
    else:
        eat_rainbow_object = EatRainbowActivity.objects.filter(date=eat_date, user=user)
        if not eat_rainbow_object:
            prev_date = get_previous_date(eat_date)
            user_object = User.objects.get(id=use_id)
            previous_object_data = EatRainbowActivity.objects.filter(date=prev_date, user=user)
            user_tag = user_object.tag.filter().values_list('id', flat=True)
            eat_masters = EatRainbowMaster.objects.filter(tag__id__in=user_tag).distinct().order_by("sequence")
            # todo handle previous date not exist
            # for the first time user is assigned to which sequence?

            if not previous_object_data:
                previous_object_data = EatRainbowActivity.objects.filter(user=user).order_by("date").last()
                previous_date = previous_object_data.date
                previous_date_str = previous_date.strftime("%Y-%m-%d")
                previous_sequence = previous_object_data.master.sequence
                diffrence_current_date = get_difference_from_current_date(previous_date_str)
                eat_rainbow_master_object = eat_masters.filter(
                    sequence=(previous_sequence + diffrence_current_date)).first()
            else:
                previous_sequence = previous_object_data.first().master.sequence
                eat_rainbow_master_object = eat_masters.filter(sequence=(previous_sequence + 1)).first()
            if not eat_rainbow_master_object:
                eat_rainbow_master_object = eat_masters.first()

            eat_rainbow_object, created = EatRainbowActivity.objects.update_or_create(user=user_object, date=eat_date,
                                                                                      defaults={
                                                                                          'master': eat_rainbow_master_object,
                                                                                          'red_serving': eat_rainbow_master_object.red_serving,
                                                                                          'cream_serving': eat_rainbow_master_object.cream_serving,
                                                                                          'yellow_serving': eat_rainbow_master_object.yellow_serving,
                                                                                          'kiwi_serving': eat_rainbow_master_object.kiwi_serving,
                                                                                          'blue_serving': eat_rainbow_master_object.blue_serving,
                                                                                          'green_serving': eat_rainbow_master_object.green_serving})

            eat_rainbow_object.enjoy_regular.set(eat_rainbow_master_object.enjoy_regular.all(), clear=True)
            eat_rainbow_object.eat_more.set(eat_rainbow_master_object.eat_more.all(), clear=True)
            eat_rainbow_object.eat_less.set(eat_rainbow_master_object.eat_less.all(), clear=True)
            eat_rainbow_object.eat_avoid.set(eat_rainbow_master_object.eat_avoid.all(), clear=True)
            eat_rainbow_object.tag.set(eat_rainbow_master_object.tag.all(), clear=True)
            eat_rainbow_object.save()
        else:
            eat_rainbow_object = eat_rainbow_object.first()

    return render(request, "main.html", {"eat_date": eat_date, "eat_rainbow_object": eat_rainbow_object})

# Exercise Activity


