from django.db import models


class TagMaster(models.Model):
    name = models.CharField(verbose_name="Tag name", max_length=100)

    def __str__(self):
        return self.name


class CategoryMaster(models.Model):
    title = models.CharField(verbose_name="Category Title", max_length=100)

    def __str__(self):
        return self.title
