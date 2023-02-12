from rest_framework import serializers

from apps.warehouse.models import ReturnedInvoice


class ReturnedInvoiceUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReturnedInvoice
        fields = (
            "id",
            "description",
        )

    def validate(self, attrs):
        instance = self.instance
        if instance.status == ReturnedInvoice.Statuses.CONFIRMED:
            raise serializers.ValidationError(
                {
                    "keys": "status_is_confirmed",
                    "error": "cannot update confirmed invoice"
                }
            )
        return attrs
