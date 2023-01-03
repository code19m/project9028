from django.db import models

from apps.warehouse.models.group import Group


class Product(models.Model):

    class Types(models.TextChoices):
        RAW = 'raw'
        FINAL = 'final'

    title = models.CharField(max_length=30, unique=True)
    code = models.CharField(max_length=4, unique=True)
    shelf_life = models.DurationField()
    current_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    product_type = models.CharField(max_length=5, choices=Types.choices, db_index=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_index=True)
    description = models.TextField(blank=True)

    added_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
