# Generated by Django 4.2 on 2023-06-05 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_cliente_disponible_cliente_domicilio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='disponible',
            field=models.BooleanField(default=True, verbose_name='Disponibilidad'),
        ),
    ]
