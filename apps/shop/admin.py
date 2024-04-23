from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'title', 'slug']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['subcategory', 'title', 'slug', 'manufacturer', 'amount', 'price', 'available']
    list_filter = ['available']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ['title']}