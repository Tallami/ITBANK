# Generated by Django 4.1 on 2022-09-06 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Sucursales", "0003_sucursal_loan_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sucursal",
            name="loan_id",
        ),
    ]
