from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField

from apps.users.managers.user import CustomUserManager
from apps.utils.mixins import ModelMixin
from apps.utils.validators import phone_regex


def get_default_role():
    return [User.Roles.DEFAULT]


class ChoiceArrayField(ArrayField):
    """
    A field that allows us to store an array of choices.
    Uses Django's Postgres ArrayField
    and a MultipleChoiceField for its formfield.
    """

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.MultipleChoiceField,
            'choices': self.base_field.choices,
        }
        defaults.update(kwargs)
        # Skip our parent's formfield implementation completely as we don't
        # care for it.
        # pylint:disable=bad-super-call
        return super(ArrayField, self).formfield(**defaults)


class User(ModelMixin, AbstractUser):

    class Roles(models.TextChoices):
        DIRECTOR = "director"
        WAREHOUSEMAN = "warehouseman"
        SALESMAN = "salesman"
        FINANCIER = "financier"
        DEFAULT = "default"

    email = models.EmailField(unique=True, blank=True)

    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)

    phone_number = models.CharField(max_length=15, blank=True,
                                    validators=(phone_regex,))

    image = models.ImageField(upload_to='photos/%y/%m/%d',
                              null=True, blank=True)

    roles = ChoiceArrayField(
        models.CharField(max_length=12, choices=Roles.choices),
        default=get_default_role
    )

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
