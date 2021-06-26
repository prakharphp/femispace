from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . import serializers
from activity.models import EatRainbowActivity
from master.models import Food, TagMaster, ExerciseActivityMaster, EatRainbowMaster
from users.models import User
from datetime import datetime
import datetime as dt
from django.db.models import Max


class EatActivityApiViewSet(viewsets.ModelViewSet):
    queryset = EatRainbowActivity.objects.prefetch_related(
         "enjoy_regular", "eat_more", "eat_less", "eat_avoid", "tag",
    ).all()
    serializer_class = serializers.EatActivitySerializer
    permission_classes = (AllowAny,)

    @action(
        detail=False,
        methods=['POST'],
        url_path=r"eat-rainbow-details",
        serializer_class=serializers.EatActivitySerializer
    )
    def get_date_user(self, request):
        user = request.data.get('user_id')
        date = request.data.get('date')
        eat_rainbow_object = EatRainbowActivity.objects.filter(date=date, user=user)
        if not eat_rainbow_object:
            user_object = User.objects.get(id=user)
            user_tag = user_object.tag.filter().values_list('id', flat=True)
            master_object = EatRainbowMaster.objects.filter(tag__id__in=user_tag).distinct().order_by("order")
            date_object = datetime.strptime(date, "%Y-%m-%d")
            day = dt.timedelta(days=1)
            reduce_date = date_object - day
            reduce_date_str = reduce_date.strftime("%Y-%m-%d")
            previous_object_data = EatRainbowActivity.objects.get(date=reduce_date_str)
            previous_assigned_data = previous_object_data.previous_date_data
            order = previous_assigned_data.order
            # count = EatRainbowMaster.objects.aggregate(Max('order'))
            # if order != count.get('order__max'):
            if master_object.last() == previous_assigned_data:
                eat_rainbow_master_object = EatRainbowActivity.objects.create(previous_date_data=master_object.first(), date=date, user=user_object)
            else:
                eat_rainbow_master_object = EatRainbowMaster.objects.filter(order=(order+1)).order_by("order").first()
                previous_assigned_data = EatRainbowActivity.objects.create(previous_date_data=eat_rainbow_master_object, date=date, user=user_object)

            # else:
            #     order = 1
            #     eat_rainbow_master_object = EatRainbowMaster.objects.filter(order=order).order_by("order").first()

            # fetch from master
            # create record in activity
            # store in eat_rainbow_object
            eat_rainbow_object = EatRainbowActivity.objects.update_or_create(user=user_object, date=date, defaults={'red_serving': eat_rainbow_master_object.red_serving,
                                                          'cream_serving':eat_rainbow_master_object.cream_serving, 'yellow_serving': eat_rainbow_master_object.yellow_serving,
                                                          'kiwi_serving': eat_rainbow_master_object.kiwi_serving, 'blue_serving': eat_rainbow_master_object.blue_serving,
                                                          'green_serving':  eat_rainbow_master_object.green_serving, })
            enjoy_regular = Food.objects.filter(id__in=eat_rainbow_master_object.enjoy_regular)
            eat_rainbow_object.enjoy_regular.set(enjoy_regular, clear=True)
            eat_more = Food.objects.filter(id__in=eat_rainbow_master_object.eat_more)
            eat_rainbow_object.eat_more.set(eat_more, clear=True)
            eat_less = Food.objects.filter(id__in=eat_rainbow_master_object.eat_less)
            eat_rainbow_object.eat_less.set(eat_less, clear=True)
            eat_avoid = Food.objects.filter(id__in=eat_rainbow_master_object.eat_avoid)
            eat_rainbow_object.eat_avoid.set(eat_avoid, clear=True)
        else:
            eat_rainbow_object = eat_rainbow_object.first()

        serializer = self.serializer_class(eat_rainbow_object).data if eat_rainbow_object else {}

        response_data = {
            "user": user,
            "date": date,
            "eat_rainbow_object": serializer
        }

        return Response(response_data)


def eat_activity(request):
    if request.method == 'GET':
        user = request.user
        print(request)
        food = Food.objects.all()
        tag = TagMaster.objects.all()
        date = request.GET.get('date')
        eat_rainbow_object = EatRainbowActivity.objects.filter(date=date, user=user)
        user_tag = user.tag.all()
        if not eat_rainbow_object:
            master_object = EatRainbowMaster.objects.filter(tag=user_tag)
            # fetch from master
            # create record in activity
            # store in eat_rainbow_object
        else:
            eat_rainbow_object = eat_rainbow_object.first()
        return render(request, "activity/eatrainbow.html", {"food": food, "tag": tag, "date": date,
                                                            "eat_rainbow": eat_rainbow_object})
    elif request.method == 'POST':
        user = request.user
        date = request.POST.get("date")
        red_serving = request.POST.get("red_serving")
        cream_serving = request.POST.get("cream_serving")
        yellow_serving = request.POST.get("yellow_serving")
        kiwi_serving = request.POST.get("kiwi_serving")
        blue_serving = request.POST.get("blue_serving")
        green_serving = request.POST.get("green_serving")
        enjoy_regular = request.POST.getlist("enjoy_regular")
        eat_more = request.POST.getlist("eat_more")
        eat_less = request.POST.getlist("eat_less")
        eat_avoid = request.POST.getlist("eat_avoid")
        tag = request.POST.getlist("tag")
        comment = request.POST.get("comment")
        obj, created = EatRainbowActivity.objects.update_or_create(user=user, date=date, defaults={'red_serving': red_serving,
                                                          'cream_serving':cream_serving, 'yellow_serving': yellow_serving,
                                                          'kiwi_serving': kiwi_serving, 'blue_serving': blue_serving,
                                                          'green_serving':  green_serving, 'comment': comment})
        # many to many fields saving from forms

        enjoy_regular = Food.objects.filter(id__in=enjoy_regular)
        obj.enjoy_regular.set(enjoy_regular, clear=True)
        eat_more = Food.objects.filter(id__in=eat_more)
        obj.eat_more.set(eat_more, clear=True)
        eat_less = Food.objects.filter(id__in=eat_less)
        obj.eat_less.set(eat_less, clear=True)
        eat_avoid = Food.objects.filter(id__in=eat_avoid)
        obj.eat_avoid.set(eat_avoid, clear=True)
        tag = TagMaster.objects.filter(id__in=tag)
        obj.tag.set(tag, clear=True)
        return render(request, "dashboard.html", {})


def exercise_activity(request):
    user = request.user
    if request.method == 'GET':
        exercise = ExerciseActivityMaster.objects.all()
        tag = TagMaster.objects.all()
        date = request.GET.get('date')
        return render(request, "avtivity/exercise_activity.html", {"tag": tag, "exercise": exercise, })
    elif request.method == 'POST':
        date = request.POST.get("date")
        exercise = request.POST.getlist("date")
        duration = request.POST.get("duration")
        met = request.POST.get("met")
        calories = request.POST.get("calories")
        feeling = request.POST.get("feeling")
        comment = request.POST.get("comment")
        tag = request.POST.getlist("tag")
        obj, created = ExerciseActivityMaster.objects.update_or_create(user=user, date=date, defaults={})





