from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import contacts, one_product, ProductView, ProductsListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/', ProductsListView.as_view(), name='products'),
    path('one_product/<int:pk>', one_product, name='one_product'),

]
