from django.shortcuts import render
from apps.shop.forms import Search
from apps.shop.models import *

# Create your views here.


def home(request):
    return render(request, 'templates/main.html')


def promotions(request):
    form = Search()
    return render(request, 'templates/promotions.html', {'form': form})


def catalog(request):
    form = Search()
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return render(request, 'templates/catalog.html', {'form': form, 'categories': categories, 'subcategories': subcategories})


# def product_search(request):
#     if 'search_field' in request.GET:
#         form = Search(request.GET)
#         return render(request, 'main/search.html')

def subcatalog_products(request, pk):
    form = Search()
    subcatelog = Subcategory.objects.get(category_id=pk)
    products = Product.objects.filter(subcategory_id=pk)
    return render(request, 'templates/subcatalog_products.html', {'form': form, 'subcatalog': subcatelog , 'products': products})


def about(request):
    form = Search()
    return render(request, 'templates/about.html', {'form': form})
