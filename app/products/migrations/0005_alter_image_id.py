# Generated by Django 4.0.8 on 2023-01-11 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_id_alter_product_inventory_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]