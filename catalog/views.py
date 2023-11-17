from django.shortcuts import render

from catalog.models import Product


def home(request):
    latest_product = Product.objects.order_by('date_of_creation',)[:5]
    print(latest_product)
    return render(request, "main/home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"От {name} ({phone}) получено сообщение: {message}")
    return render(request, "main/contacts.html")
