from django.core.files.images import ImageFile
from django.core.management import BaseCommand
from django.db import transaction

from apps.finance.models import Income, Expense
from apps.sales.models import Client
from apps.users.models import User
from apps.warehouse.models import (
    Brand, Group, Product, Supplier,
    InputInvoice, InputInvoiceItem,
    OutputInvoice, OutputInvoiceItem,
    ReturnedInvoice, ReturnedInvoiceItem,
)
from apps.warehouse.management.commands.fakes.fake_clients import clients
from apps.warehouse.management.commands.fakes.fake_expenses import expenses
from apps.warehouse.management.commands.fakes.fake_invoices import (
    input_invoices,
    output_invoices,
    returned_invoices
)
from apps.warehouse.management.commands.fakes.fake_invoice_items import (
    input_invoice_items,
    output_invoice_items,
    returned_invoice_items
)
from apps.warehouse.management.commands.fakes.fake_incomes import incomes
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

        for input_invoice in input_invoices:
            InputInvoice.objects.create(**input_invoice)

        for input_item in input_invoice_items:
            InputInvoiceItem.objects.create(**input_item)

        for output_invoice in output_invoices:
            OutputInvoice.objects.create(**output_invoice)

        for output_item in output_invoice_items:
            OutputInvoiceItem.objects.create(**output_item)

        for returned_invoice in returned_invoices:
            ReturnedInvoice.objects.create(**returned_invoice)

        for returned_item in returned_invoice_items:
            ReturnedInvoiceItem.objects.create(**returned_item)

        for expense in expenses:
            Expense.objects.create(**expense)

        for income in incomes:
            Income.objects.create(**income)

        confirmed_input_invoices = InputInvoice.objects.filter(status=InputInvoice.Statuses.CONFIRMED)
        for invoice in confirmed_input_invoices:
            invoice.update_products_quantity()

        confirmed_output_invoices = OutputInvoice.objects.filter(status=OutputInvoice.Statuses.CONFIRMED)
        for invoice in confirmed_output_invoices:
            invoice.update_products_quantity()

        print("DB populated successfully!!!")
