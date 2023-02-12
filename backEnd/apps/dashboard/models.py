from django.db import models
from django.utils import timezone


class Goal(models.Model):
    intended_amount = models.IntegerField()
    achieved_amount = models.IntegerField(default=0)

    added_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    @classmethod
    def get_current_goal(cls):
        current_year = timezone.now().year
        current_month = timezone.now().month
        return cls.objects.filter(
            added_time__year=current_year,
            added_time__month=current_month
        ).first()
