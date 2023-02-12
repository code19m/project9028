from django.db import models

from apps.warehouse.models.input_invoice import InputInvoice
from apps.warehouse.models.returned_invoice import ReturnedInvoice


class Expense(models.Model):

    invoice = models.ForeignKey(
        InputInvoice, on_delete=models.CASCADE, db_index=True, null=True, related_name="expenses"
    )
    returned_invoice = models.ForeignKey(
        ReturnedInvoice, on_delete=models.CASCADE, db_index=True, null=True, related_name="expenses"
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)

    added_time = models.DateTimeField(auto_now_add=True)
