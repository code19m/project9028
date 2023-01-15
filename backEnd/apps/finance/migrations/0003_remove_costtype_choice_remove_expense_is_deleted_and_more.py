# Generated by Django 4.0.4 on 2023-01-15 15:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_costtype_is_deleted_expense_is_deleted_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costtype',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='income',
            name='is_deleted',
        ),
        migrations.AddField(
            model_name='expense',
            name='added_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='expense',
            name='cost_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='finance.costtype'),
        ),
    ]
