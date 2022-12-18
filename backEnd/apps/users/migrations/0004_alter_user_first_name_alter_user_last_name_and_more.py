# Generated by Django 4.0.4 on 2022-12-18 09:51

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_username_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('director', 'Director'), ('warehouseman', 'Warehouseman'), ('salesman', 'Salesman'), ('financier', 'Financier'), ('default', 'Default')], max_length=12), default=['default'], size=None),
        ),
    ]
