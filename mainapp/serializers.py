from .models import Category, CartProduct, Product, ProductSpecification
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField


class ProductSpecificationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSpecification
        fields = ['specification_name', 'value']


class ProductSerializer(serializers.ModelSerializer):

    product_specification = ProductSpecificationsSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['product_title', 'product_specification']


class CartProductSerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = CartProduct
        fields = ['cart_product_title','unique_data', 'products' ]


class OnePageResultSerializer(serializers.ModelSerializer):

    children = RecursiveField(many=True)
    cart_products = CartProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'children', 'cart_products']
#