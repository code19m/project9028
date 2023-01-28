from rest_framework import serializers

from apps.warehouse.serializers.supplier import SupplierSerializer
from apps.warehouse.models import InputInvoice


class InputInvoiceGetSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()
    total_sum = serializers.DecimalField(max_digits=20, decimal_places=2, allow_null=False)
    paid_sum = serializers.DecimalField(max_digits=20, decimal_places=2, allow_null=False)

    class Meta:
        model = InputInvoice
        fields = (
            "id",
            "supplier",
            "status",
            "total_sum",
            "paid_sum",
            "description",
            "added_time",
        )
