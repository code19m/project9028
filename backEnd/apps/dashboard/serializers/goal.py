from django.utils import timezone
from rest_framework import serializers

from apps.dashboard.models import Goal


class GoalCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = (
            "id",
            "intended_amount",
        )


class GoalGetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = (
            "id",
            "intended_amount",
            "achieved_amount",
            "added_time",
        )


class GoalUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = (
            "id",
            "intended_amount",
        )

    def validate(self, attrs):
        added_time = self.instance.added_time

        current_year = timezone.now().year
        current_month = timezone.now().month

        if added_time.year < current_year or added_time.month < current_month:
            raise serializers.ValidationError({
                "key": "id",
                "error": "Only current goal is editable"
            })

        return attrs
