from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogView, BlogListView, BlogDetailsView, BlogUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('articles/', BlogListView.as_view(), name='articles'),
    path('detail/<int:pk>', BlogDetailsView.as_view(), name='blog_detail'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
]
