from rest_framework import serializers

from apps.sales.serializers.client import ClientSerializer
from apps.warehouse.models import OutputInvoice


class OutputInvoiceGetSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    total_sum = serializers.DecimalField(max_digits=20, decimal_places=2, allow_null=False)
    paid_sum = serializers.DecimalField(max_digits=20, decimal_places=2, allow_null=False)

    class Meta:
        model = OutputInvoice
        fields = (
            "id",
            "client",
            "status",
            "total_sum",
            "paid_sum",
            "description",
            "added_time",
        )
