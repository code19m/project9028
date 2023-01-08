from rest_framework import serializers

from apps.warehouse.models import Group


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = (
            "id",
            "title",
        )
