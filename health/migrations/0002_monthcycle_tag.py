# Generated by Django 3.2.4 on 2021-06-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_alter_tagmaster_tag_type'),
        ('health', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthcycle',
            name='tag',
            field=models.ManyToManyField(blank=True, to='master.TagMaster'),
        ),
    ]