from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class InvalidURLException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_code = _("invalid_url")
    default_detail = _(
        "A product does not exist in this url or the product cannot be processed by us."
    )


class InvalidProductDetailsException(APIException):
    status_code = status.HTTP_406_NOT_ACCEPTABLE
    default_code = _("invalid_product_details")
    default_detail = _("Atleast one of the details provided is invalid.")
