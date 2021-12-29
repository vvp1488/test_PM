from django.contrib import admin
from .models import Category, ProductSpecification, Product, CartProduct
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin


admin.site.register(Category, DraggableMPTTAdmin)

admin.site.register(ProductSpecification)
admin.site.register(Product)
admin.site.register(CartProduct, DraggableMPTTAdmin)

