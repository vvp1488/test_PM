from django.urls import path
from .views import CategoryListAPIView, ProductListAPIView, OnePageResult
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.myapp.com",
      contact=openapi.Contact(email="admin@ukr.net"),
      license=openapi.License(name="Test License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('products/<int:pk>', ProductListAPIView.as_view(), name='product_list'),
    path('one_page_result/', OnePageResult.as_view(), name='result'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
