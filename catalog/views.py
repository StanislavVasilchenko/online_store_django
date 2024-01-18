from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, CreateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ModerationForm
from catalog.models import Product, Version, Category
from catalog.services import get_cache_categories, get_cache_category_detail


class UserPassesMixin(UserPassesTestMixin):
    """Класс миксин для проверки является ли пользолватель владельцем продукта или модератором.
    Используется для редактирования или удаления продукта."""

    def test_func(self):
        user = self.request.user
        product = self.get_object()
        if product.owner == user:
            return True
        elif user.groups.filter(name='moderator').exists():
            return True
        return self.handle_no_permission()


class ProductView(TemplateView):
    """Класс для отображения главной страницы"""
    model = Product
    template_name = 'catalog/index.html'

    def get_context_data(self, *args, **kwargs):
        """Функция для изменения колтчества выводимыъ продуктов на главной странице.
        Вывод 4 любых продуктов."""
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()[:4]
        return context_data


class ProductsListView(ListView):
    """Класс для отображения всех существующих продуктов"""
    model = Product

    def get_context_data(self, **kwargs):
        """Функия для передачи в контеуст версии продукта. Если продукт имеет активный статус,
        то название версии будет отбражено на странице. """
        context_data = super().get_context_data(**kwargs)
        context_data['version'] = Version.objects.all()
        return context_data


class ProductsDetailView(LoginRequiredMixin, DetailView):
    """Класс для отображения детального описания конкретного продукта"""
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Класс для отображения страниы создания продукта"""
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        """функция которая определяет текущего залогиненого пользоателя, который добавляет прдукт"""
        new_product = form.save()
        new_product.owner = self.request.user
        new_product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesMixin, UpdateView):
    """Класс для отображения страницы для изменения продукта.
    Изменить продукт могут только пользователь добавивший данный продукт или имеющий доступ для изменения."""
    model = Product
    permission_required = 'catalog.change_product'
    form_class = ProductForm

    def get_success_url(self):
        """Функция для перенаправления пользователя на страницу продукта который был изменен"""
        return reverse('catalog:product_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        """Функция для отображения версии продукта на страницы редактирования.
        Использует inlineformset_factory и передает донные в контекст"""
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        """Функция для формы изменения версии продукта"""
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_form_class(self):
        """Функция для представления формы пользователю являющемуся модератором."""
        if self.request.user.is_staff:
            return ModerationForm
        else:
            return ProductForm


class ProductDeleteView(LoginRequiredMixin, UserPassesMixin, DeleteView):
    """Класс для отображения страницы удаления продукта"""
    model = Product
    success_url = reverse_lazy('catalog:home')


class ContactView(TemplateView):
    """Класс для представления страницы контактов"""
    template_name = 'catalog/contacts.html'
    success_url = 'catalog/'

    @staticmethod
    def post(request):
        """Функция для получения из формы данных от пользователя"""
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"От {name} ({phone}) получено сообщение: {message}")
        return HttpResponseRedirect(reverse('catalog:contacts'))


class CategoryView(TemplateView):
    model = Category
    template_name = 'catalog/category_index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = get_cache_categories()
        return context_data


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = get_cache_category_detail(self.object.pk)
        return context_data
