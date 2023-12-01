from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from blog.models import Blog


class BlogView(TemplateView):
    template_name = 'blog/index_blog.html'


class BlogCreateView(CreateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image', 'publication_sign')
    success_url = reverse_lazy('blog:home')




