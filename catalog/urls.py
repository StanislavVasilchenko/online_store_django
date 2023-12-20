from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import ProductView, ProductsListView, ProductsDetailView, ContactView, ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductView.as_view(), name='home'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('one_product/<int:pk>', ProductsDetailView.as_view(), name='one_product'),
    path('product_create/', ProductCreateView.as_view(), name='product_create'),

]
