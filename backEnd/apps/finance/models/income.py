from django.db import models

from apps.warehouse.models.output_invoice import OutputInvoice


class Income(models.Model):
    
    class Types(models.TextChoices):
        FROM_OUTSIDE = "from_outside"
        FROM_SALES = "from_sales"

    income_type = models.CharField(max_length=15, choices=Types.choices, db_index=True)
    invoice = models.ForeignKey(OutputInvoice, on_delete=models.CASCADE, db_index=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    added_time = models.DateTimeField(auto_now_add=True)

    is_deleted = models.BooleanField(default=False)
