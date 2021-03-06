# Generated by Django 3.2.4 on 2021-06-21 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_auto_20210621_1445'),
        ('activity', '0004_auto_20210621_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='day',
            name='activity',
        ),
        migrations.RemoveField(
            model_name='day',
            name='breakfast_meal',
        ),
        migrations.RemoveField(
            model_name='day',
            name='brunch_meal',
        ),
        migrations.RemoveField(
            model_name='day',
            name='dinner_meal',
        ),
        migrations.RemoveField(
            model_name='day',
            name='eve_snacks_meal',
        ),
        migrations.RemoveField(
            model_name='day',
            name='evening_exercise',
        ),
        migrations.RemoveField(
            model_name='day',
            name='lunch_meal',
        ),
        migrations.RemoveField(
            model_name='day',
            name='morning_exercise',
        ),
        migrations.RemoveField(
            model_name='day',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='drinkingactivitymaster',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='eatrainbowmaster',
            name='eat_avoid',
        ),
        migrations.RemoveField(
            model_name='eatrainbowmaster',
            name='eat_less',
        ),
        migrations.RemoveField(
            model_name='eatrainbowmaster',
            name='eat_more',
        ),
        migrations.RemoveField(
            model_name='eatrainbowmaster',
            name='enjoy_regular',
        ),
        migrations.RemoveField(
            model_name='eatrainbowmaster',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='exerciseactivitymaster',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='exerciseactivitymaster',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='exercisemaster',
            name='tag_master',
        ),
        migrations.RemoveField(
            model_name='program',
            name='days',
        ),
        migrations.RemoveField(
            model_name='program',
            name='drinking_exercise',
        ),
        migrations.RemoveField(
            model_name='program',
            name='eat_rainbow',
        ),
        migrations.RemoveField(
            model_name='program',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='program',
            name='meditation',
        ),
        migrations.RemoveField(
            model_name='program',
            name='preferred_for',
        ),
        migrations.RemoveField(
            model_name='program',
            name='sugar_intake',
        ),
        migrations.RemoveField(
            model_name='program',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='sugarintakeactivitymaster',
            name='dessert_snack',
        ),
        migrations.RemoveField(
            model_name='sugarintakeactivitymaster',
            name='dried_fruits',
        ),
        migrations.RemoveField(
            model_name='sugarintakeactivitymaster',
            name='drink_juices',
        ),
        migrations.RemoveField(
            model_name='sugarintakeactivitymaster',
            name='fruits',
        ),
        migrations.RemoveField(
            model_name='sugarintakeactivitymaster',
            name='sweet_veggie',
        ),
        migrations.AlterField(
            model_name='addcustomactivity',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.activitymaster'),
        ),
        migrations.AlterField(
            model_name='eatrainbowactivity',
            name='eat_avoid',
            field=models.ManyToManyField(blank=True, related_name='eat_avoid_user', to='master.Food', verbose_name='Avoid eat'),
        ),
        migrations.AlterField(
            model_name='eatrainbowactivity',
            name='eat_less',
            field=models.ManyToManyField(blank=True, related_name='eat_less_user', to='master.Food'),
        ),
        migrations.AlterField(
            model_name='eatrainbowactivity',
            name='eat_more',
            field=models.ManyToManyField(blank=True, related_name='eat_more_user', to='master.Food'),
        ),
        migrations.AlterField(
            model_name='eatrainbowactivity',
            name='enjoy_regular',
            field=models.ManyToManyField(blank=True, related_name='enjoy_regular_user', to='master.Food'),
        ),
        migrations.AlterField(
            model_name='exerciseactivity',
            name='exercise',
            field=models.ManyToManyField(blank=True, to='master.ExerciseMaster'),
        ),
        migrations.AlterField(
            model_name='sugarintakeactivity',
            name='dessert_snacks',
            field=models.ManyToManyField(blank=True, related_name='dessert_snacks_user', to='master.Food'),
        ),
        migrations.AlterField(
            model_name='sugarintakeactivity',
            name='dried_fruit',
            field=models.ManyToManyField(blank=True, related_name='dry_fruit_user', to='master.Food'),
        ),
        migrations.AlterField(
            model_name='sugarintakeactivity',
            name='drink_juice',
            field=models.ManyToManyField(blank=True, related_name='drink_juice_user', to='master.Food'),
        ),
        migrations.AlterField(
            model_name='sugarintakeactivity',
            name='fruit',
            field=models.ManyToManyField(blank=True, related_name='fruit_user', to='master.Food'),
        ),
        migrations.AlterField(
            model_name='sugarintakeactivity',
            name='sweet_veggies',
            field=models.ManyToManyField(blank=True, related_name='sweet_vaggies_user', to='master.Food'),
        ),
        migrations.AlterField(
            model_name='userplan',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.program'),
        ),
        migrations.DeleteModel(
            name='ActivityMaster',
        ),
        migrations.DeleteModel(
            name='Day',
        ),
        migrations.DeleteModel(
            name='DrinkingActivityMaster',
        ),
        migrations.DeleteModel(
            name='EatRainbowMaster',
        ),
        migrations.DeleteModel(
            name='ExerciseActivityMaster',
        ),
        migrations.DeleteModel(
            name='ExerciseMaster',
        ),
        migrations.DeleteModel(
            name='MeditationMaster',
        ),
        migrations.DeleteModel(
            name='Program',
        ),
        migrations.DeleteModel(
            name='SugarIntakeActivityMaster',
        ),
    ]
