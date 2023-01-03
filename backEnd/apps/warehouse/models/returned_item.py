from django.db import models

from apps.warehouse.models.product import Product
from apps.warehouse.models.returned_invoice import ReturnedInvoice


class ReturnedInvoiceItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_index=True)
    invoice = models.ForeignKey(ReturnedInvoice, on_delete=models.CASCADE, db_index=True)

    quantity = models.DecimalField(max_digits=5, decimal_places=1)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
