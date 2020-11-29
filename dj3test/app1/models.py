
from django.db import models

from faker import Faker

fake = Faker()


class A(models.Model):
    bla = models.CharField(max_length=250, default=fake.pystr)

    def __str__(self):
        return f"{self.bla}"


class B(models.Model):
    x = models.IntegerField(default=fake.pyint)
    a = models.ForeignKey(to=A, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}: {self.x} {self.a}"


class D(models.Model):
    meh = models.CharField(max_length=250, default=fake.pystr)


def new_d():
    return D.objects.create().id


class C(models.Model):
    title = models.CharField(max_length=250, default=fake.pystr)
    b = models.ForeignKey(to=B, on_delete=models.CASCADE)
    d = models.ForeignKey(to=D, on_delete=models.CASCADE, default=new_d)

    @property
    def dmeh(self):
        return self.d.meh

    def __str__(self):
        return f"{self.id}: {self.b}"
