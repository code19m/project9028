from django.db import models


class Brand(models.Model):
    title = models.CharField(max_length=30)

    is_deleted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
