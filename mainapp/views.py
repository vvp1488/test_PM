from .serializers import CategorySerializer, ProductSerializer, OnePageResultSerializer

from rest_framework import  generics
from .models import Category, Product, Catalog


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter()
    serializer_class = CategorySerializer


class ProductListAPIView(generics.ListAPIView):

    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get_queryset(self):
        queryset = Product.objects.root_nodes().filter(category=self.kwargs['pk'])
        return queryset


class OnePageResult(generics.ListAPIView):

    serializer_class = OnePageResultSerializer
    queryset = Catalog.objects.all()

