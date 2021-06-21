from django.contrib import admin
from .models import *
# Register your models here.


class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name", "unit"]

    class Meta:
        model = Ingredient


class RecipeAdmin(admin.ModelAdmin):
    list_display = ["title", "picture", "nutrition"]

    class Meta:
        model = Recipe


class FoodAdmin(admin.ModelAdmin):
    list_display = ["name", "quantity_g", "unit"]

    class Meta:
        model = Food


class MealAdmin(admin.ModelAdmin):
    list_display = ["title", "get_prefer_time_display", "intake_duration"]

    class Meta:
        model = Meal

class ExerciseActivityMasterAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "duration_min", "calories_burn"]

    class Meta:
        model = ExerciseActivityMaster


class ProgramAdmin(admin.ModelAdmin):
    filter_horizonal = ('days',)
    list_display = ["title", "day_count"]

    class Meta:
        model = Program


admin.site.register(Nutrition)
admin.site.register(IngredientAlias)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredients)
admin.site.register(Food, FoodAdmin)
admin.site.register(Meal, MealAdmin)

admin.site.register(TagMaster)
admin.site.register(CategoryMaster)
admin.site.register(Banners)
admin.site.register(Lesson)
admin.site.register(HealthCourses)
admin.site.register(ActivityMaster)
admin.site.register(ExerciseMaster)
admin.site.register(ExerciseActivityMaster, ExerciseActivityMasterAdmin)
admin.site.register(EatRainbowMaster)
admin.site.register(DrinkingActivityMaster)
admin.site.register(SugarIntakeActivityMaster)
admin.site.register(MeditationMaster)
admin.site.register(Program, ProgramAdmin)