import json
import os
from django.shortcuts import render
from django.http import HttpResponse
from goddamit.models import Product, ProductCategories

MODULE_DIR = os.path.dirname(__file__)


def read_file(name):
    file_path = os.path.join(MODULE_DIR, name)
    return json.load(open(file_path, encoding='utf-8'))


def index(request):
    content = {
        'title': 'GeekShop'
    }
    return render(request, 'goddamit/index.html', content)


def products(request):
    products = read_file('fixtures/products.json')
    categories = read_file('fixtures/categories.json')

    content = {
        'title': 'GeekShop - Katalog',
        'categories': ProductCategories.objects.all(),
        'products': Product.objects.all()
    }

    return render(request, 'goddamit/products.html', content)
