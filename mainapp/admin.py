from django.contrib import admin
from .models import Category, Product, Catalog
from mptt.admin import MPTTModelAdmin


class CatalogAdmin(admin.ModelAdmin):

    list_display = ('group_item_name','slug')

admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Category)
admin.site.register(Product, MPTTModelAdmin)
