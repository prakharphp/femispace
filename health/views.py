from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from health.models import MonthCycle, AverageCycle
from . import serializers
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
import datetime as dt
from .utils import get_all_dates_in_month


class MonthCycleApiViewSet(viewsets.ModelViewSet):
    queryset = MonthCycle.objects.prefetch_related(
         "tag", "feeling"
    ).all()
    serializer_class = serializers.MonthCycleSerializer
    permission_classes = (AllowAny,)

    @action(
        detail=False,
        methods=['GET'],
        url_path=r"user-month-details",
        serializer_class=serializers.MonthCycleSerializer
    )
    def get_cycle_by_date(self, request):
        """
        filter by date and year
        for each date match the data  give the data predicted if actual is provided then pridicted data match with actual
        """
        user = request.query_params.get('user_id')
        date = request.query_params.get('date')
        date_str = date.split("-")
        year = date_str[0]
        month = date_str[1]
        user_cycle_detail_by_date = MonthCycle.objects.filter(user=user, date__year__gte=year, date__month__gte=month).order_by("date")
        date_object = self.serializer_class(user_cycle_detail_by_date, many=True).data if user_cycle_detail_by_date else {}
        dict = {}
        date_by_month = get_all_dates_in_month(year, month)
        for i in range(len(date_by_month)):
            cycle_obj_by_date = user_cycle_detail_by_date.filter(date=date_by_month[i])
            if not cycle_obj_by_date.first():
                pass
                # average_cycle = AverageCycle.objects.get(user=user)
                # mesturation_phase = date + dt.timedelta(days=average_cycle.menstruation_days)
                # follicular_phase = mesturation_phase + dt.timedelta(days=average_cycle.follicular_days)

            else:
                pass
                # check the is_actual if yes then show it as it is else get predicted data
            dict[date_by_month[i]] = "red"
        response_data = {
            "year": year,
            "user": user,
            "date_object": date_object,
            "results": dict,
        }

        return Response(response_data)