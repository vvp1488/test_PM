# Generated by Django 4.0 on 2021-12-29 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_remove_productnew_title_productnew_product_title_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='cart_product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_specification',
        ),
        migrations.AddField(
            model_name='cartproductnew',
            name='unique_data',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='productnew',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productnew',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='productnew',
            name='product_specification',
            field=models.ManyToManyField(related_name='all_specifications', to='mainapp.ProductSpecification'),
        ),
        migrations.DeleteModel(
            name='CartProduct',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
