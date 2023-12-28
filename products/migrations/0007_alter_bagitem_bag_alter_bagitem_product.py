# Generated by Django 4.2.6 on 2023-12-27 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0006_alter_bagitem_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bagitem",
            name="bag",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bagitems",
                to="products.bag",
            ),
        ),
        migrations.AlterField(
            model_name="bagitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="items",
                to="products.products",
            ),
        ),
    ]
