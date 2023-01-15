from django.db import models

from apps.warehouse.models.product import Product
from apps.warehouse.models.output_invoice import OutputInvoice


class OutputInvoiceItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True)
    invoice = models.ForeignKey(
        OutputInvoice, on_delete=models.CASCADE, db_index=True, related_name="items"
    )

    quantity = models.DecimalField(max_digits=5, decimal_places=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
