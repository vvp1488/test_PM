# Generated by Django 4.0 on 2021-12-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_catalog_category_slug_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=255),
        ),
    ]