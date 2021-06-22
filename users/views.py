from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,HttpResponse

from master.models import Food, TagMaster
from users.serializers import UserSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from users.models import User
from . import serializers
from django.contrib import messages
from health.models import HealthModule
from activity.models import EatRainbowActivity


class UserApiViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (AllowAny, )


# def get_eating_habit(request):
#     user = request.POST.get('id')
#     date = request.POST.get('date',)
#     obj = User.objects.get(id=int(user))
#     tag = obj.tag


def user_login(request):
    return render(request, "login.html", {})


def login_request(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return render(request, "dashboard.html", {})
    else:
        messages.error(request, "invalid email or password")


def health_module(request):
    if request.method == 'GET':
        return render(request, "healthModule.html")
    elif request.method == 'POST':
        user = request.user
        on_medication = request.POST.get('on_medication')
        doctors_name = request.POST.get('doctors_name')
        prescrption = request.POST.get('prescrption')
        had_surgery = request.POST.get('had_surgery')
        diabetes = request.POST.get('diabetes')
        heart_issues = request.POST.get('heart_issues')
        mental_issue = request.POST.get('mental_issue')
        additonal_info = request.POST.get('additonal_info')
        obj = HealthModule.objects.create(user=user, on_medication=on_medication, doctors_name=doctors_name,
                                          prescrption=prescrption, had_surgery=had_surgery, diabetes=diabetes,
                                          heart_issues=heart_issues, mental_issue=mental_issue, additonal_info=additonal_info)
        obj.save()
        return render(request, "dashboard.html", {})


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
        return render(request, "eatrainbow.html", {"food": food, "tag": tag, "date": date, "eat_rainbow":eat_rainbow_object})
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

# def save_many_to_many(key)