from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, UpdateView, CreateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ModerationForm
from catalog.models import Product, Version


class UserPassesMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        product = self.get_object()
        if product.owner == user:
            return True
        elif user.groups.filter(name='moderator').exists():
            return True
        return self.handle_no_permission()


class ProductView(TemplateView):
    model = Product
    template_name = 'catalog/index.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()[:4]
        return context_data


class ProductsListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['version'] = Version.objects.all()
        return context_data


class ProductsDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:products')

    def form_valid(self, form):
        new_product = form.save()
        new_product.owner = self.request.user
        new_product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesMixin, UpdateView):
    model = Product
    permission_required = 'catalog.change_product'
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:product_update', args=[self.kwargs.get('pk')])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_form_class(self):
        if self.request.user.is_staff:
            return ModerationForm
        else:
            return ProductForm


class ProductDeleteView(LoginRequiredMixin, UserPassesMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:home')


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'
    success_url = 'catalog/'

    @staticmethod
    def post(request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"От {name} ({phone}) получено сообщение: {message}")
        return HttpResponseRedirect(reverse('catalog:contacts'))
