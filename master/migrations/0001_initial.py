# Generated by Django 3.2.4 on 2021-06-19 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Category Title')),
            ],
        ),
        migrations.CreateModel(
            name='TagMaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_type', models.PositiveSmallIntegerField(choices=[(1, 'Symptoms'), (2, 'Cycle')], default=1)),
                ('name', models.CharField(max_length=100, verbose_name='Tag name')),
            ],
        ),
    ]
