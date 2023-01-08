from django.db import models

from apps.sales.models.client import Client


class OutputInvoice(models.Model):
    
    class Statuses(models.TextChoices):
        NEW = "new"
        CONFIRMED = "confirmed"

    client = models.ForeignKey(Client, on_delete=models.CASCADE, db_index=True)

    status = models.CharField(max_length=10, choices=Statuses.choices, default=Statuses.NEW)
    description = models.TextField(blank=True)

    added_time = models.DateTimeField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)
