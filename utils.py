from enum import Enum


class EnumValuesMixin:

   @classmethod
   def values(cls):
       return [e.value for e in cls]


class A(EnumValuesMixin, Enum):
    X = 10
    Y = 20


print(A.values())
