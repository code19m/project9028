from django.db import models

from utils.validators import phone_regex


class Client(models.Model):
    title = models.CharField(max_length=30)
    phone_number = models.CharField(
        max_length=15, blank=True, validators=(phone_regex,)
    )
    address = models.TextField(blank=True)
