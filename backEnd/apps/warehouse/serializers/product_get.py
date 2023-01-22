from rest_framework import serializers

from apps.warehouse.models.product import Product
from apps.warehouse.serializers.group import GroupSerializer
from apps.warehouse.serializers.brand import BrandSerializer


class ProductGetSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    brand = BrandSerializer()

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "code",
            "current_arrival_price",
            "current_selling_price",
            "brand",
            "group",
            "image",
            "description",
            "added_time",
        )


class ProductNestedSerializer(serializers.ModelSerializer):
    """
        Nested serializer for invoice items
    """

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "code",
        )
