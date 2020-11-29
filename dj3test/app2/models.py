from django.db import models

from faker import Faker

fake = Faker()


class Author(models.Model):
    name = models.CharField(max_length=150, default=fake.name)


class Book(models.Model):
    title = models.CharField(max_length=150, default=fake.sentence)
    price = models.IntegerField(default=fake.pyint)
    author = models.OneToOneField(to=Author, related_name="bla", related_query_name="bla2", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.title} [${self.price}]"
