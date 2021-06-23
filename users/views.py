from django.contrib.auth import authenticate, login
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from users.models import User
from . import serializers
from django.contrib import messages
from health.models import HealthModule



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



# def save_many_to_many(key)