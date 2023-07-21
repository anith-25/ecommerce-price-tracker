from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "url",
            "image",
            "initial_price",
            "current_price",
            "cuttoff_price",
            "amount_discount",
            "added_on",
        ]
