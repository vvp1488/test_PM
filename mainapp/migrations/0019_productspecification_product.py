# Generated by Django 4.0 on 2021-12-29 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_rename_cartproductnew_cartproduct_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productspecification',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='item', to='mainapp.product'),
            preserve_default=False,
        ),
    ]