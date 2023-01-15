from rest_framework import serializers

from apps.warehouse.models import OutputInvoice


class OutputInvoiceAddSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutputInvoice
        fields = (
            "id",
            "client",
            "description",
        )
    
    def validate_client(self, value):
        if value.is_deleted:
            raise serializers.ValidationError(
                {
                    "keys": "deleted_client",
                    "error": "given client is deleted"
                }
            )
        return value
