# Generated by Django 3.2.4 on 2021-06-19 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('master', '0001_initial'),
        ('activity', '0001_initial'),
        ('health', '0001_initial'),
        ('food', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userplan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sugarintakeactivity',
            name='dessert_snacks',
            field=models.ManyToManyField(blank=True, related_name='dessert_snacks_user', to='food.Food'),
        ),
        migrations.AddField(
            model_name='sugarintakeactivity',
            name='dried_fruit',
            field=models.ManyToManyField(blank=True, related_name='dry_fruit_user', to='food.Food'),
        ),
        migrations.AddField(
            model_name='sugarintakeactivity',
            name='drink_juice',
            field=models.ManyToManyField(blank=True, related_name='drink_juice_user', to='food.Food'),
        ),
        migrations.AddField(
            model_name='sugarintakeactivity',
            name='fruit',
            field=models.ManyToManyField(blank=True, related_name='fruit_user', to='food.Food'),
        ),
        migrations.AddField(
            model_name='sugarintakeactivity',
            name='sweet_veggies',
            field=models.ManyToManyField(blank=True, related_name='sweet_vaggies_user', to='food.Food'),
        ),
        migrations.AddField(
            model_name='sugarintakeactivity',
            name='tag',
            field=models.ManyToManyField(blank=True, to='master.TagMaster'),
        ),
        migrations.AddField(
            model_name='sugarintakeactivity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='program',
            name='days',
            field=models.ManyToManyField(to='activity.Day'),
        ),
        migrations.AddField(
            model_name='program',
            name='preferred_for',
            field=models.ManyToManyField(blank=True, to='health.WellnessArea'),
        ),
        migrations.AddField(
            model_name='program',
            name='tag',
            field=models.ManyToManyField(blank=True, to='master.TagMaster'),
        ),
        migrations.AddField(
            model_name='meditationactivity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='exerciseactivitymaster',
            name='exercise',
            field=models.ManyToManyField(blank=True, to='activity.ExerciseMaster'),
        ),
        migrations.AddField(
            model_name='exerciseactivitymaster',
            name='tag',
            field=models.ManyToManyField(blank=True, to='master.TagMaster'),
        ),
        migrations.AddField(
            model_name='exerciseactivity',
            name='exercise',
            field=models.ManyToManyField(blank=True, to='activity.ExerciseMaster'),
        ),
        migrations.AddField(
            model_name='exerciseactivity',
            name='tag',
            field=models.ManyToManyField(blank=True, to='master.TagMaster'),
        ),
        migrations.AddField(
            model_name='exerciseactivity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='eatrainbowmaster',
            name='eat_avoid',
            field=models.ManyToManyField(blank=True, related_name='eat_avoid_master', to='food.Food', verbose_name='Avoid eat'),
        ),
        migrations.AddField(
            model_name='eatrainbowmaster',
            name='eat_less',
            field=models.ManyToManyField(blank=True, related_name='eat_less_master', to='food.Food'),
        ),
        migrations.AddField(
            model_name='eatrainbowmaster',
            name='eat_more',
            field=models.ManyToManyField(blank=True, related_name='eat_more_master', to='food.Food'),
        ),
        migrations.AddField(
            model_name='eatrainbowmaster',
            name='enjoy_regular',
            field=models.ManyToManyField(blank=True, related_name='enjoy_regular_master', to='food.Food'),
        ),
        migrations.AddField(
            model_name='eatrainbowmaster',
            name='tag',
            field=models.ManyToManyField(blank=True, to='master.TagMaster'),
        ),
        migrations.AddField(
            model_name='eatrainbowactivity',
            name='eat_avoid',
            field=models.ManyToManyField(blank=True, related_name='eat_avoid_user', to='food.Food', verbose_name='Avoid eat'),
        ),
        migrations.AddField(
            model_name='eatrainbowactivity',
            name='eat_less',
            field=models.ManyToManyField(blank=True, related_name='eat_less_user', to='food.Food'),
        ),
        migrations.AddField(
            model_name='eatrainbowactivity',
            name='eat_more',
            field=models.ManyToManyField(blank=True, related_name='eat_more_user', to='food.Food'),
        ),
        migrations.AddField(
            model_name='eatrainbowactivity',
            name='enjoy_regular',
            field=models.ManyToManyField(blank=True, related_name='enjoy_regular_user', to='food.Food'),
        ),
        migrations.AddField(
            model_name='eatrainbowactivity',
            name='tag',
            field=models.ManyToManyField(blank=True, to='master.TagMaster'),
        ),
        migrations.AddField(
            model_name='eatrainbowactivity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='drinkingwateractivity',
            name='tag',
            field=models.ManyToManyField(blank=True, to='master.TagMaster'),
        ),
        migrations.AddField(
            model_name='drinkingwateractivity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='day',
            name='activity',
            field=models.ManyToManyField(blank=True, to='activity.ActivityMaster'),
        ),
        migrations.AddField(
            model_name='day',
            name='breakfast_meal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='breakfast', to='food.meal'),
        ),
        migrations.AddField(
            model_name='day',
            name='brunch_meal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brunch', to='food.meal'),
        ),
        migrations.AddField(
            model_name='day',
            name='dinner_meal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dinner', to='food.meal'),
        ),
        migrations.AddField(
            model_name='day',
            name='eve_snacks_meal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eve_snack', to='food.meal'),
        ),
        migrations.AddField(
            model_name='day',
            name='evening_exercise',
            field=models.ManyToManyField(blank=True, related_name='evening_exercise_list', to='activity.ExerciseMaster'),
        ),
        migrations.AddField(
            model_name='day',
            name='lunch_meal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lunch', to='food.meal'),
        ),
        migrations.AddField(
            model_name='day',
            name='morning_exercise',
            field=models.ManyToManyField(blank=True, related_name='morning_exercise_list', to='activity.ExerciseMaster'),
        ),
        migrations.AddField(
            model_name='day',
            name='tag',
            field=models.ManyToManyField(blank=True, to='master.TagMaster'),
        ),
        migrations.AddField(
            model_name='addcustomactivity',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity.activitymaster'),
        ),
        migrations.AddField(
            model_name='activitymaster',
            name='tag',
            field=models.ManyToManyField(blank=True, to='master.TagMaster'),
        ),
    ]
