from rest_framework import serializers

from apps.warehouse.models.product import Product
from apps.warehouse.serializers.group import GroupSerializer


class ProductGetSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    
    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "code",
            "shelf_life",
            "current_price",
            "product_type",
            "group",
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
