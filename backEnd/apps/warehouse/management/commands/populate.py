from django.core.files.images import ImageFile
from django.core.management import BaseCommand
from django.db import transaction

from apps.sales.models import Client
from apps.users.models import User
from apps.warehouse.models import Brand, Group, Product, Supplier
from apps.warehouse.management.commands.fakes.fake_clients import clients
from apps.warehouse.management.commands.fakes.fake_products import (
    groups,
    brands,
    products
)
from apps.warehouse.management.commands.fakes.fake_suppliers import suppliers
from apps.warehouse.management.commands.fakes.fake_users import users


class Command(BaseCommand):
    help = "populate command populates empty db with example data"

    @transaction.atomic
    def handle(self, *args, **options):
        product_images_directory = "apps/warehouse/management/commands/fakes/product_images"

        for user in users:
            password = user.pop("password")
            user = User(**user)
            user.set_password(password)
            user.save()

        for supplier in suppliers:
            Supplier.objects.create(**supplier)

        for client in clients:
            Client.objects.create(**client)

        for brand in brands:
            Brand.objects.create(**brand)

        for group in groups:
            Group.objects.create(**group)

        for product in products:
            image_name = product.pop('image')
            image_path = f"{product_images_directory}/{image_name}"
            pr = Product.objects.create(
                **product
            )
            with open(image_path, "rb") as file:
                pr.image = ImageFile(file, image_name)
                pr.save()

        print("DB populated successfully!!!")
