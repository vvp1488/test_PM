# Generated by Django 4.0 on 2021-12-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_remove_productspecification_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_specification',
        ),
        migrations.AddField(
            model_name='product',
            name='product_specification',
            field=models.ManyToManyField(related_name='all_specifications', to='mainapp.ProductSpecification'),
        ),
    ]
