from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

from activity.models import EatRainbowActivity
from activity.utils import get_difference_from_current_date, get_previous_date
from master.models import EatRainbowMaster
from users.models import User
from . import serializers
from django.contrib import messages
from health.models import HealthModule
import datetime


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
    user = request.user
    use_id = user.id
    if request.POST.get('eat_date'):
        eat_date = request.POST.get('eat_date')
    else:
        eat_date = datetime.date

    eat_rainbow_object = EatRainbowActivity.objects.filter(date=eat_date, user=user)
    if not eat_rainbow_object:
        prev_date = get_previous_date(eat_date)
        user_object = User.objects.get(id=use_id)
        previous_object_data = EatRainbowActivity.objects.filter(date=prev_date, user=user)
        user_tag = user_object.tag.filter().values_list('id', flat=True)
        eat_masters = EatRainbowMaster.objects.filter(tag__id__in=user_tag).distinct().order_by("sequence")
        ## todo handle previous date not exist
        # if not previous_object_data:
        #     previous_object_data = EatRainbowActivity.objects.filter(user=user).order_by("date")
        #     previous_date = previous_object_data.date
        #     previous_date_object = datetime.strptime(previous_date, "%Y-%m-%d")
        #     previous_sequence = previous_object_data.last().master.sequence
        #     diffrence_current_date = get_difference_from_current_date(previous_date_object)
        #     eat_rainbow_master_object = eat_masters.filter(
        #         sequence=(previous_sequence + diffrence_current_date)).first()
        # else:
        #     previous_sequence = previous_object_data.first().master.sequence
        #     eat_rainbow_master_object = eat_masters.filter(sequence=(previous_sequence + 1)).first()
        # if not eat_rainbow_master_object:
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

    return render(request, "main.html", {"eat_date":eat_date, "eat_rainbow_object":eat_rainbow_object})

#
# def login_request(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#     user = authenticate(request, email=email, password=password)
#     if user is not None:
#         login(request, user)
#         return render(request, "dashboard.html", {})
#     else:
#         messages.error(request, "invalid email or password")
#
#
# def health_module(request):
#     if request.method == 'GET':
#         return render(request, "healthModule.html")
#     elif request.method == 'POST':
#         user = request.user
#         on_medication = request.POST.get('on_medication')
#         doctors_name = request.POST.get('doctors_name')
#         prescrption = request.POST.get('prescrption')
#         had_surgery = request.POST.get('had_surgery')
#         diabetes = request.POST.get('diabetes')
#         heart_issues = request.POST.get('heart_issues')
#         mental_issue = request.POST.get('mental_issue')
#         additonal_info = request.POST.get('additonal_info')
#         obj = HealthModule.objects.create(user=user, on_medication=on_medication, doctors_name=doctors_name,
#                                           prescrption=prescrption, had_surgery=had_surgery, diabetes=diabetes,
#                                           heart_issues=heart_issues, mental_issue=mental_issue, additonal_info=additonal_info)
#         obj.save()
#         return render(request, "dashboard.html", {})
#
#

# def save_many_to_many(key)