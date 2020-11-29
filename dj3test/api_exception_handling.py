from rest_framework.exceptions import APIException
from rest_framework.views import exception_handler as rest_framework_exception_handler


def exception_handler(exc, context):
    response = rest_framework_exception_handler(exc, context)

    if isinstance(exc, APIException):

        if isinstance(exc.detail, (list, dict)):
            data = {
                'code': 'multiple',
                'errors': exc.get_full_details(),
            }
        else:
            data = {
                'code': exc.detail.code,
                'message': exc.detail,
            }

        response.data = data

    return response
