
from rest_framework import serializers as ser

from .models import A, B, C


class CSerializer(ser.ModelSerializer):

    class Meta:
        model = C
        fields = ('title', 'dmeh',)


class BSubSerializer(ser.ModelSerializer):
    c_items = CSerializer(source='c_set', many=True)

    class Meta:
        model = B
        fields = (
            'x', 'c_items',
        )


class ASerializer(ser.ModelSerializer):
    b_items = BSubSerializer(source='b_set', many=True)

    class Meta:
        model = A
        fields = (
            'bla',
            'b_items',
        )


class BSerializer(ser.ModelSerializer):
    class Meta:
        model = B
        fields = ('x', 'a',)
