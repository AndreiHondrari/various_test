from rest_framework import generics, viewsets
from django_filters import rest_framework as filters

from .models import A, B
from .serializers import ASerializer, BSerializer


class AListView(generics.ListAPIView):
    # queryset = A.objects.all()
    queryset = A.objects.prefetch_related(
        "b_set",
        "b_set__c_set",
        "b_set__c_set__d",
    )
    serializer_class = ASerializer


class ARetrieveView(generics.RetrieveAPIView):
    queryset = A.objects.all()
    serializer_class = ASerializer


class BFilterSet(filters.FilterSet):

    class Meta:
        model = B
        fields = {
            'a': ['exact', 'in'],
        }


class BListView(generics.ListAPIView):
    queryset = B.objects.all()
    serializer_class = BSerializer
    filterset_class = BFilterSet


class BRetrieveView(generics.RetrieveAPIView):
    queryset = B.objects.all()
    serializer_class = BSerializer


class AViewset(viewsets.ModelViewSet):
    queryset = A.objects.prefetch_related(
        "b_set",
        "b_set__c_set",
    )
    serializer_class = ASerializer
