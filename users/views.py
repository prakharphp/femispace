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
        food = Food.objects.all()
        tag = TagMaster.objects.all()
        return render(request, "eatrainbow.html", {"food": food, "tag": tag})
    elif request.method == 'POST':
        user = request.user
        red_serving = request.POST.get("red_serving")
        cream_serving = request.POST.get("cream_serving")
        yellow_serving = request.POST.get("yellow_serving")
        kiwi_serving = request.POST.get("kiwi_serving")
        blue_serving = request.POST.get("blue_serving")
        green_serving = request.POST.get("green_serving")
        enjoy_regular = request.POST.get("enjoy_regular")
        eat_more = request.POST.get("eat_more")
        eat_less = request.POST.get("eat_less")
        eat_avoid = request.POST.get("eat_avoid")
        tag = request.POST.get("tag")
        obj = EatRainbowActivity.objects.create(user=user, red_serving=red_serving, cream_serving=cream_serving,
                                                yellow_serving=yellow_serving,
                                                kiwi_serving=kiwi_serving, blue_serving=blue_serving,
                                                green_serving=green_serving,
                                                enjoy_regular=enjoy_regular, eat_more=eat_more, eat_less=eat_less,
                                                eat_avoid=eat_avoid, tag=tag)
        obj.save()
        return render(request, "dashboard.html", {})