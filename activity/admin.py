from django.contrib import admin

from .models import *


class DayAdmin(admin.ModelAdmin):
    # form = DayForm
    list_display = ["title", "breakfast_meal", "brunch_meal", "lunch_meal", "eve_snacks_meal", "dinner_meal"]

    class Meta:
        model = Day



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


class EatRAinbowActivityAdmin(admin.ModelAdmin):
    # form = DayForm
    list_display = ["date", "user", "is_actual", "red_serving", "cream_serving", "yellow_serving", "kiwi_serving",
                    "blue_serving", "green_serving"]

    class Meta:
        model = EatRainbowActivity


admin.site.register(Day, DayAdmin)
admin.site.register(EatRainbowActivity, EatRAinbowActivityAdmin)
admin.site.register(ExerciseActivity)
admin.site.register(DrinkingWaterActivity)
admin.site.register(SugarIntakeActivity)
admin.site.register(MeditationActivity)
admin.site.register(UserPlan)





