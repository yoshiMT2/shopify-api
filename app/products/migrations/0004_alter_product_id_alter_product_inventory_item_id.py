# Generated by Django 4.0.8 on 2023-01-11 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_product_id_image_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='inventory_item_id',
            field=models.BigIntegerField(),
        ),
    ]
