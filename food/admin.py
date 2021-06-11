from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple

from .models import *
from django import forms


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


admin.site.register(Nutrition)
admin.site.register(IngredientAlias)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredients)
admin.site.register(Food, FoodAdmin)
admin.site.register(Meal, MealAdmin)
