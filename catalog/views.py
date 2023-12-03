from django.views.generic import ListView, TemplateView, DetailView

from catalog.models import Product


class ProductView(TemplateView):
    model = Product
    template_name = 'catalog/index.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()[:4]
        return context_data


class ProductsListView(ListView):
    model = Product


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'


class ContactView(TemplateView):
    template_name = 'catalog/contacts.html'

    def post(self, request):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"От {name} ({phone}) получено сообщение: {message}")
        return self.render_to_response(self.get_context_data())
