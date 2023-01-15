from rest_framework import serializers

from apps.warehouse.models import OutputInvoice


class OutputInvoiceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = OutputInvoice
        fields = (
            "id",
            "description",
            "status",
        )

    def validate(self, attrs):
        instance = self.instance
        if instance.status == OutputInvoice.Statuses.CONFIRMED:
            raise serializers.ValidationError(
                {
                    "keys": "status_is_confirmed",
                    "error": "cannot update confirmed invoice"
                }
            )
        return attrs
