from django.db import models


class CostType(models.Model):
    title = models.CharField(max_length=30)

    is_deleted = models.BooleanField(default=False)
