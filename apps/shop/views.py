from django.shortcuts import render
from django.views.generic import ListView
from apps.shop.models import *

# Create your views here.


def home(request):
    return render(request, 'templates/main.html')


def promotions(request):
    return render(request, 'templates/promotions.html')


def catalog(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    return render(request, 'templates/catalog.html', {'categories': categories, 'subcategories': subcategories})


class Search(ListView):
    template_name = 'templates/search.html'
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


def subcatalog_products(request, pk):
    subcatelog = Subcategory.objects.get(category_id=pk)
    products = Product.objects.filter(subcategory_id=pk)
    return render(request, 'templates/subcatalog_products.html', {'subcatalog': subcatelog , 'products': products})


def about(request):
    return render(request, 'templates/about.html')
