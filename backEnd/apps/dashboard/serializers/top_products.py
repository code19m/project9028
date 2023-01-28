from rest_framework import serializers

from apps.warehouse.models import Product


class TopProductsSerializer(serializers.ModelSerializer):
    total_sales = serializers.DecimalField(max_digits=20, decimal_places=2, allow_null=False)

    class Meta:
        model = Product
        fields = (
            "id",
            "title",
            "code",
            "total_sales",
        )
