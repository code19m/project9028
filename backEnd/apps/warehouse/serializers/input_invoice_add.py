from rest_framework import serializers

from apps.warehouse.models import InputInvoice


class InputInvoiceAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = InputInvoice
        fields = (
            "id",
            "supplier",
            "description",
        )
