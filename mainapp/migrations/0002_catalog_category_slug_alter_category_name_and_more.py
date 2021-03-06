# Generated by Django 4.0 on 2021-12-28 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(auto_created=True)),
                ('group_item_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(auto_created=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='catalog_group_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='all_category', to='mainapp.catalog'),
            preserve_default=False,
        ),
    ]
