from django.db import models


class TagMasterChoices(models.IntegerChoices):
    symptoms = 1
    tag = 2


class TagMaster(models.Model):
    tag_type = models.PositiveSmallIntegerField(choices=TagMasterChoices.choices, default=TagMasterChoices.symptoms)
    name = models.CharField(verbose_name="Tag name", max_length=100)

    def __str__(self):
        return self.name


class CategoryMaster(models.Model):
    title = models.CharField(verbose_name="Category Title", max_length=100)

    def __str__(self):
        return self.title
