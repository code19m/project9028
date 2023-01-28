from rest_framework import serializers

from apps.warehouse.models import InputInvoice


class InputInvoiceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = InputInvoice
        fields = (
            "id",
            "description",
        )

    def validate(self, attrs):
        instance = self.instance
        if instance.status == InputInvoice.Statuses.CONFIRMED:
            raise serializers.ValidationError(
                {
                    "keys": "status_is_confirmed",
                    "error": "cannot update confirmed invoice"
                }
            )
        return attrs
