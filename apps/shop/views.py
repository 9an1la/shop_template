from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.shop.filters import ProductFilter
from apps.shop.models import *
from apps.cart.forms import CartAddProductForm
from apps.shop.recommender import Recommender
from apps.shop.api.serializers import CategoryListSerializer


# Create your views here.


def home(request):
    return render(request, 'shop/home.html')


def promotions(request):
    return render(request, 'shop/promotions.html')


def catalog(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return render(request, 'shop/catalog.html', {'categories': categories, 'subcategories': subcategories})


class Search(ListView):
    template_name = 'shop/search.html'
    context_object_name = 'product_search'
    paginate_by = 5

    def get_queryset(self):
        title_search = Product.objects.filter(title__icontains=self.request.GET.get('q'))
        manufacturer_search = Product.objects.filter(manufacturer__icontains=self.request.GET.get('q'))
        res = title_search | manufacturer_search
        return res.distinct()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context


def subcatalog_products(request, subcategory_slug=None):
    subcategory = None
    subcategories = Subcategory.objects.all()
    products = Product.objects.filter(available=True)
    filters = ProductFilter(request.GET, queryset=Product.objects.all())
    if subcategory_slug:
        subcategory = get_object_or_404(Subcategory, slug=subcategory_slug)
        products = products.filter(subcategory=subcategory)
    return render(request, 'shop/subcatalog_products.html', {'subcategory': subcategory, 'products': products, 'filters': filters})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    r = Recommender()
    recommended_products = r.suggest_products_for([product], 4)
    return render(request, 'shop/product_detail.html',
                  {'product': product, 'cart_product_form': cart_product_form,
                   'recommended_products': recommended_products})


def about(request):
    return render(request, 'shop/about.html')
