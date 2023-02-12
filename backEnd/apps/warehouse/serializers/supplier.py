from rest_framework import serializers

from apps.warehouse.models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    credit = serializers.DecimalField(max_digits=20, decimal_places=2, allow_null=False)

    class Meta:
        model = Supplier
        fields = (
            "id",
            "title",
            "credit",
            "address",
        )
