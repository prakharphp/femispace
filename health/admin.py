from django.contrib import admin
from .models import *


class WellnessAreaAdmin(admin.ModelAdmin):
    list_display = ["title"]

    class Meta:
        model = WellnessArea


class MonthCycleAdmin(admin.ModelAdmin):
    list_display = ["user", "date", "is_menstruation", "is_follicular", "is_ovulation", "is_luteal", "is_pre_menstruation",
                    "is_actual", "updated_at", "created_at"]

    class Meta:
        model = MonthCycle


class AverageCycleAdmin(admin.ModelAdmin):
    list_display = ["user", "menstruation_days", "follicular_days", "proliferative_days", "luteal_days",
                    "secretory_days", "updated_at"]

    class Meta:
        model = AverageCycle


admin.site.register(WellnessArea, WellnessAreaAdmin)
admin.site.register(MonthCycle, MonthCycleAdmin)
admin.site.register(AverageCycle, AverageCycleAdmin)
admin.site.register(HealthModule)
