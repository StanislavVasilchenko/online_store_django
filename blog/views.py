from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from blog.models import Blog


class BlogView(TemplateView):
    template_name = 'blog/index_blog.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Blog.objects.all()[:4]
        return context_data


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image', 'publication_sign')
    success_url = reverse_lazy('blog:home')


class BlogDetailsView(DetailView):
    model = Blog


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image', 'publication_sign')
    success_url = reverse_lazy('blog:home')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.object.id])
