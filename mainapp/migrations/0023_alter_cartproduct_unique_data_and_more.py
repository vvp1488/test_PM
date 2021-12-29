# Generated by Django 4.0 on 2021-12-29 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_remove_product_product_specification_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartproduct',
            name='unique_data',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_specification',
            field=models.ManyToManyField(to='mainapp.ProductSpecification'),
        ),
    ]