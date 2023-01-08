from django.db import models


class Supplier(models.Model):
    title = models.CharField(max_length=50, unique=True)
    address = models.TextField(blank=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
