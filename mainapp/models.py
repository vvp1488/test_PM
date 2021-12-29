from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.dispatch import receiver
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from django.db.models.signals import m2m_changed

# class Catalog(models.Model):
#
#     group_item_name = models.CharField(max_length=255, unique=True)
#
#     slug = models.SlugField(
#         default='',
#         editable=False,
#         max_length=255,
#     )
#
#     def save(self, *args, **kwargs):
#         value = self.group_item_name
#         self.slug = slugify(value, allow_unicode=True)
#         super().save(*args, **kwargs)
#
#     def __str__(self):
#         return self.group_item_name


class Category(MPTTModel):

    category_name = models.CharField(max_length=255, unique=True)
    is_parent = models.BooleanField()
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

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

    class MPTTMeta:
        order_insertion_by = ['category_name']


class ProductSpecification(models.Model):

    specification_name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return '{} - {}'.format(self.specification_name, self.value)


class CartProduct(MPTTModel):

    cart_product_title = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='cart_products')
    unique_data = models.TextField(max_length=255, blank=True)

    def __str__(self):
        return self.cart_product_title

    class MPTTMeta:
        order_insertion_by = ['cart_product_title']


class Product(MPTTModel):

    product_title = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey(CartProduct, on_delete=models.CASCADE, null=True, blank=True, related_name='products')
    product_specification = models.ManyToManyField(ProductSpecification)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ['product_title']

    def __str__(self):
        return self.product_title

    def delete(self, *args, **kwargs):
        cart_product = CartProduct.objects.get(cart_product_title=str(self.parent))
        unique_data = str(cart_product.unique_data)
        x = unique_data.split('\n')
        qs = self.product_specification.all()
        for item in qs:
            if str(item) in x:
                x.remove(str(item))
        cart_product.unique_data = ''
        for item in x:
            cart_product.unique_data += '%s\n' % str(item)
            cart_product.save()
        super(Product, self).delete(*args, **kwargs)



@receiver(m2m_changed, sender=Product.product_specification.through)
def product_specification_change(sender, action, pk_set, instance=None, **kwargs):
    if action == 'post_add':
        queryset = instance.product_specification.all()
        cart_product = CartProduct.objects.get(cart_product_title=instance.parent)
        unique_data = str(cart_product.unique_data)
        for item in queryset:
            if str(item) not in unique_data:
                cart_product.unique_data += '%s\n' % str(item)
                cart_product.save()








# class Product(MPTTModel):
#
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
#     product_name = models.CharField(max_length=255, unique=True)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
#     is_active = models.BooleanField(default=True)
#     is_parent = models.BooleanField()
#     parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
#
#     def __str__(self):
#         return self.product_name
#
#     class MPTTMeta:
#         order_insertion_by = ['product_name']

