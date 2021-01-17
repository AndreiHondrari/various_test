import uuid

from django.db import models


class StrNameMixin:

    def __str__(self):
        return f"{self.name}"


class Country(StrNameMixin, models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Countries"


class Region(StrNameMixin, models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)


class Address(StrNameMixin, models.Model):
    name = models.CharField(max_length=200)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    region = models.ForeignKey(to=Region, on_delete=models.CASCADE)
