# Generated by Django 4.0 on 2021-12-28 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_rename_name_category_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='product_name',
        ),
    ]
