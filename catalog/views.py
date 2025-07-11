import logging

from catalog.apps import CatalogProjectConfig


from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, f"{CatalogProjectConfig.name}/home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        return render(request, f"{CatalogProjectConfig.name}/response.html")
    return render(request, f"{CatalogProjectConfig.name}/contacts.html")
