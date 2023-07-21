from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import InvalidProductDetailsException, InvalidURLException
from .models import Product
from .pagination import StandardResultsPagination
from .scrap import get_link_data
from .serializers import ProductSerializer


class ScrapProductAPIView(APIView):
    def post(self, request, *args, **kwargs):
        url = request.data.get("url")
        product_details = get_link_data(url)
        if product_details:
            return Response(data=product_details)
        else:
            raise InvalidURLException


class ProductListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all().order_by("-added_on")
        paginator = StandardResultsPagination()
        page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)


class AddProductAPIView(APIView):
    def post(self, request, *args, **kwargs):
        product_name = request.data.get("product_name")
        product_url = request.data.get("product_url")
        image = request.data.get("image")
        price = request.data.get("price")
        cuttoff_price = request.data.get("cuttoff_price") or None

        try:
            product = Product.objects.create(
                name=product_name,
                url=product_url,
                image=image,
                initial_price=price,
                current_price=price,
                cuttoff_price=cuttoff_price,
            )
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Exception:
            raise InvalidProductDetailsException
