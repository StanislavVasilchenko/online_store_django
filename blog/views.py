from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.templatetags.pytils_translit import slugify

from blog.models import Blog


class CreateUpdateMixin:
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image', 'publication_sign')

    def get_success_url(self):
        """Переренаправляет пользователя после создания статьи на созданную статью"""
        return reverse('blog:blog_detail', args=[self.object.id, self.object.slug])

    def form_valid(self, form):
        """Переводит название статьи в слаг"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.blog_title)
            new_blog.save()
        return super().form_valid(form)


class BlogListView(ListView):
    """Класс для отображения статей блога"""
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """Фильтр для фильтрации статей из БД только со статусом публикации True"""
        queryset = super().get_queryset()
        queryset = queryset.filter(publication_sign=True)
        return queryset


class BlogCreateView(CreateUpdateMixin, CreateView):
    """Класс для отображения страницы создания статьи. Наследует методы перенапоавления
     и создания слага от CreateUpdateMixin"""


class BlogDetailsView(DetailView):
    """Класс для отобрадения конкретной статьи блога"""
    model = Blog

    def get_object(self, queryset=None):
        """При переходе к статье блога увеличивает счетчик просмотров"""
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(CreateUpdateMixin, UpdateView):
    """Класс для отображения страницы редактирования статьи блогаю Наследует методы перенапоавления
     и создания слага от CreateUpdateMixin"""


class BlogDeleteView(DeleteView):
    """Класс для отображения страницы удаления статьи"""
    model = Blog
    success_url = reverse_lazy('blog:articles')
