# Generated by Django 3.2.4 on 2021-06-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0006_alter_userplan_program'),
    ]

    operations = [
        migrations.AddField(
            model_name='eatrainbowactivity',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
