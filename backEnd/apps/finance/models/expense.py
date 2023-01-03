from django.db import models

from apps.finance.models.cost_type import CostType
from apps.warehouse.models.input_invoice import InputInvoice
from apps.warehouse.models.returned_invoice import ReturnedInvoice


class Expense(models.Model):
    cost_type = models.ForeignKey(CostType, on_delete=models.CASCADE)
    input_invoice = models.ForeignKey(InputInvoice, on_delete=models.CASCADE, db_index=True, null=True)
    returned_invoice = models.ForeignKey(ReturnedInvoice, on_delete=models.CASCADE, db_index=True, null=True)
