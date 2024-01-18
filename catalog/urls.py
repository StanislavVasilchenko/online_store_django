from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductView, ProductsListView, ProductsDetailView, ContactView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, CategoryView, CategoryDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('one_product/<int:pk>', cache_page(60)(ProductsDetailView.as_view()), name='one_product'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),
    path('product_update/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('categories_prod/<int:pk>', CategoryDetailView.as_view(), name='categories_prod'),
    path('categories/', CategoryView.as_view(), name='categories'),

]
