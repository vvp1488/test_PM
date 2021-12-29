from .serializers import OnePageResultSerializer

from rest_framework import  generics
from .models import Category


class OnePageResult(generics.ListAPIView):

    serializer_class = OnePageResultSerializer

    def get_queryset(self):
        queryset = Category.objects.root_nodes().all()
        return queryset


