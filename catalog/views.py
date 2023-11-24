from django.shortcuts import render

from catalog.models import Product, Category


def home(request):
    context = {
        'product_list': Product.objects.order_by('date_of_creation')[:4]
    }
    return render(request, "main/home.html", context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"От {name} ({phone}) получено сообщение: {message}")
    return render(request, "main/contacts.html")


def products(request):
    context = {
        'product_list': Product.objects.all()
    }
    return render(request, "main/products.html", context)


def one_product(request, pk):
    context = {
        'product_list': Product.objects.filter(id=pk)
    }
    print(context)
    return render(request, "main/one_product.html", context)





