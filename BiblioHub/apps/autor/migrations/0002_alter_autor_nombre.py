# Generated by Django 4.2 on 2023-05-13 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.TextField(max_length=50),
        ),
    ]