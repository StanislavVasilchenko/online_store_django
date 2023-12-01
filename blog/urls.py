from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogView, BlogCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
]
