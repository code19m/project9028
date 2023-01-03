from django.db import models


class CostType(models.Model):

    class Choices(models.TextChoices):
        FOR_INPUT_INVOICE = "for_input_invoice"
        FOR_RETURNED_INVOICE = "for_returned_invoice"
        OTHER = "other"

    choice = models.CharField(max_length=20, choices=Choices.choices, default=Choices.OTHER)
    title = models.CharField(max_length=30)
