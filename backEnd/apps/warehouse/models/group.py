from django.db import models


class Group(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.title
