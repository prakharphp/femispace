from django.contrib import admin

from .models import *


class ExerciseActivityMasterAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "duration_min", "calories_burn"]

    class Meta:
        model = ExerciseActivityMaster


class ProgramAdmin(admin.ModelAdmin):
    filter_horizonal = ('days',)
    list_display = ["title", "day_count"]

    class Meta:
        model = Program


# class DayForm(forms.ModelForm):
#     days = forms.ModelChoiceField(queryset=Program.objects.all(), required=True,
#                                   widget=FilteredSelectMultiple(verbose_name='day', is_stacked=False))
#
#     def __init__(self, *args, **kwargs):
#         super(DayForm, self).__init__(*args, **kwargs)
#
#         if self.instance and self.instance.pk:
#             self.fields['days'].initial = self.instance.days.all()
#
#     class Meta:
#         model = Day
#         fields = ["title", "breakfast_meal", "brunch_meal", "lunch_meal", "eve_snacks_meal", "morning_exercise"]


class DayAdmin(admin.ModelAdmin):
    # form = DayForm
    list_display = ["title", "breakfast_meal", "brunch_meal", "lunch_meal", "eve_snacks_meal"]

    class Meta:
        model = Day


admin.site.register(ActivityMaster)
admin.site.register(ExerciseActivityMaster, ExerciseActivityMasterAdmin)
admin.site.register(ExerciseMaster)
admin.site.register(Day, DayAdmin)
admin.site.register(Program, ProgramAdmin)
admin.site.register(EatRainbowMaster)
admin.site.register(EatRainbowActivity)
admin.site.register(ExerciseActivity)
admin.site.register(DrinkingWaterActivity)
admin.site.register(SugarIntakeActivity)
admin.site.register(MeditationActivity)
