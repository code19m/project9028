from django.db import models

from apps.warehouse.models.brand import Brand
from apps.warehouse.models.group import Group


class Product(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=4)
    current_arrival_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    current_selling_price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, db_index=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, db_index=True)
    quantity = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='product_images/%y/%m/%d',
                              null=True, blank=True)

    added_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    is_deleted = models.BooleanField(default=False, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title'],
                condition=models.Q(is_deleted=False),
                name='unique_title_if_not_deleted'),
            models.UniqueConstraint(
                fields=['code'],
                condition=models.Q(is_deleted=False),
                name='unique_code_if_not_deleted')
        ]

    def __str__(self) -> str:
        return self.title
