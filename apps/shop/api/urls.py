from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='categories_list'),
    path('subcategories/', views.SubcategoryListView.as_view(), name='subcategories_list'),
    path('products/', views.ProductListView.as_view(), name='products_list'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
]