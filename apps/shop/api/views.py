from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import Category, Subcategory, Product
from .serializers import CategoryListSerializer, SubcategoryListSerializer, ProductListSerializer, ProductDetailSerializer


class CategoryListView(APIView):
    """Список категорий"""
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategoryListSerializer(categories, many=True)
        return Response(serializer.data)


class SubcategoryListView(APIView):
    """Список подкатегорий"""
    def get(self, request):
        subcategories = Subcategory.objects.all()
        serializer = SubcategoryListSerializer(subcategories, many=True)
        return Response(serializer.data)


class ProductListView(APIView):
    """Список всех товаров"""
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    """Информация о товаре"""
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)
