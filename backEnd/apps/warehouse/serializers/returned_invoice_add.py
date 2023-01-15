from rest_framework import serializers

from apps.warehouse.models import ReturnedInvoice


class ReturnedInvoiceAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReturnedInvoice
        fields = (
            "id",
            "client",
            "description",
        )
