# Generated by Django 4.0 on 2021-12-29 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_cartproduct_productspecification_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartproduct',
            name='cart_product_name',
            field=models.CharField(default=1, max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
