from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from catalog.models import Product


class ProductView(TemplateView):
    model = Product
    template_name = 'catalog/index.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()[:4]
        return context_data


# def home(request):
#     context = {
#         'product_list': Product.objects.order_by('date_of_creation')[:4]
#     }
#     return render(request, "catalog/index.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"От {name} ({phone}) получено сообщение: {message}")
    return render(request, "catalog/contacts.html")


class ProductsListView(ListView):
    model = Product
    #
    # def get_context_data(self, *args, **kwargs):
    #     context_data = super().get_context_data(*args, **kwargs)
    #     context_data['object_list'] = Product.objects.all()[:4]
    #     return context_data


# def products(request):
#     context = {
#         'product_list': Product.objects.all()
#     }
#     return render(request, "catalog/product_list.html", context)


def one_product(request, pk):
    context = {
        'product_list': Product.objects.filter(id=pk)
    }
    return render(request, "catalog/one_product.html", context)
