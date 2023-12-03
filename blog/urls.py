from django.urls import path

from blog.apps import BlogConfig
from blog.views import (BlogCreateView, BlogListView, BlogDetailsView, BlogUpdateView,
                        BlogDeleteView)

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('', BlogListView.as_view(), name='articles'),
    path('detail/<int:pk>/<slug:slug>', BlogDetailsView.as_view(), name='blog_detail'),
    path('update/<int:pk>/<slug:slug>', BlogUpdateView.as_view(), name='blog_update'),
    path('delete/<int:pk>/<slug:slug>', BlogDeleteView.as_view(), name='blog_delete'),
]
