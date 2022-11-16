from django.shortcuts import HttpResponse
from datetime import datetime
from django.shortcuts import render
# Create your views here.


def greed(request):
    if request.method == 'hello/':
        return HttpResponse('Hello! Its my project')


def date(request):
    if request.method == 'now_date/':
        today = datetime.now()
        return HttpResponse(today)

def bye(request):
    if request.method == 'goodby/':
        return HttpResponse('Goodby user!')

from products.models import Product


def main(request):
    if request.method == 'GET':
        products = Product.objects.all()

        data = {
            'products': products
        }
        return render(request, 'layouts/main.html', context=data)


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        data = {
            'products': products
        }

        return render(request, 'products/products.html', context=data)
