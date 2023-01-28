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

    def set_confirmed_status(self):
        self.status = self.Statuses.CONFIRMED
        self.save()

    def update_products_quantity(self):
        items = self.items.all()
        for item in items:
            product = item.product
            product.quantity -= item.quantity
            product.save()
