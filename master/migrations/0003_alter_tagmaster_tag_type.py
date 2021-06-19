# Generated by Django 3.2.4 on 2021-06-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_tagmaster_tag_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagmaster',
            name='tag_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Symptoms'), (2, 'Cycle')], default=1),
        ),
    ]
