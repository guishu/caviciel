from django.db.utils import IntegrityError
from rest_framework.response import Response
from rest_framework.views import exception_handler
from rest_framework import status

def custom_exception_handler(exception, context):
    response = exception_handler(exception, context)

    if response is None:
        if isinstance(exception, IntegrityError):
            if exception.args[0].endswith("not_both_null"):
                response = Response(
                    {"message": "Domain or name must be set for the producer."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            elif exception.args[0] in [
                "UNIQUE constraint failed: core_producer.name",
                "UNIQUE constraint failed: core_producer.domain",
                "UNIQUE constraint failed: core_producer.name, core_producer.domain",
            ]:
                response = Response(
                    {"message": "The pair name/domain must be unique for a producer."},
                    status=status.HTTP_409_CONFLICT
                )

    if response is not None:
        response.data["status_code"] = response.status_code

    return response
