from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify


class Catalog(models.Model):

    group_item_name = models.CharField(max_length=255, unique=True)

    slug = models.SlugField(
        default='',
        editable=False,
        max_length=255,
    )

    def save(self, *args, **kwargs):
        value = self.group_item_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.group_item_name


class Category(models.Model):

    category_name = models.CharField(max_length=255, unique=True)

    catalog_group_item = models.ForeignKey(Catalog, on_delete=models.PROTECT, related_name='all_category')

    slug = models.SlugField(
        default='',
        editable=False,
        max_length=255,
    )

    def save(self, *args, **kwargs):
        value = self.category_name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class Product(MPTTModel):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    product_name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    is_parent = models.BooleanField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.product_name

    class MPTTMeta:
        order_insertion_by = ['product_name']

