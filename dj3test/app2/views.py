from rest_framework import viewsets, exceptions
from rest_framework.exceptions import ErrorDetail

from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request, *args, **kwargs):
        raise exceptions.APIException(
            {
                "level1": [
                    ErrorDetail("level2", code="level2_code"),
                    {
                        "level3": ErrorDetail("something", code="code_for_something")
                    }
                ]
            },
            code="main_code"
        )
        # raise exceptions.APIException({
        #     "fwaf": exceptions.ErrorDetail("zzzz", code="mah")
        # })
