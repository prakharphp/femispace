from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from . import serializers
from activity.models import EatRainbowActivity
from master.models import Food, TagMaster


class EatActivityApiViewSet(viewsets.ModelViewSet):
    queryset = EatRainbowActivity.objects.all()
    serializer_class = serializers.EatActivitySerializer
    permission_classes = (AllowAny,)


def eat_activity(request):
    if request.method == 'GET':
        user = request.user
        food = Food.objects.all()
        tag = TagMaster.objects.all()
        date = request.GET.get('date')
        eat_rainbow_object = EatRainbowActivity.objects.fliter(date=date, user=user)
        if not eat_rainbow_object:
            pass
            ## fetch from master
            ## create record in activity
            ## store in eat_rainbow_object
        else:
            eat_rainbow_object = eat_rainbow_object.first()
        return render(request, "activity/eatrainbow.html", {"food": food, "tag": tag, "date": date, "eat_rainbow":eat_rainbow_object})
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