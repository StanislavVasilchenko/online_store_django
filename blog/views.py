from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
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

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image', 'publication_sign')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.object.id])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:articles')
