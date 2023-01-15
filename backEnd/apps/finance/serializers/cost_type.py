from rest_framework import serializers

from apps.finance.models import CostType


class CostTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CostType
        fields = (
            "id",
            "title",
        )
