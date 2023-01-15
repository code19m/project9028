from rest_framework import serializers

from apps.warehouse.serializers.supplier import SupplierSerializer
from apps.warehouse.models import InputInvoice


class InputInvoiceGetSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer()

    class Meta:
        model = InputInvoice
        fields = (
            "id",
            "supplier",
            "status",
            "description",
            "added_time",
        )
