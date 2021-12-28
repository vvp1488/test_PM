from .models import Category, Product, Catalog
from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    products = serializers.HyperlinkedIdentityField(view_name='product_list')

    class Meta:
        model = Category
        fields = ['id', 'category_name', 'products']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='category_name', read_only=True)
    children = RecursiveField(many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'category',
            'product_name',
            'description',
            'is_active',
            'children'
        ]


class ForOnePageResultSerializer1(serializers.ModelSerializer):

    children = RecursiveField(many=True)

    class Meta:
        model = Product
        fields = [
            'product_name',
            'children'
        ]


class ForOnePageResultSerializer(serializers.ModelSerializer):

    products = ForOnePageResultSerializer1(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['category_name', 'products']


class OnePageResultSerializer(serializers.ModelSerializer):

    all_category = ForOnePageResultSerializer(many=True, read_only=True)

    class Meta:
        model = Catalog
        fields = [
            'group_item_name',
            'all_category',
        ]