from rest_framework import serializers

from apps.shop.models import Category, Subcategory, Product


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubcategoryListSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Subcategory
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    subcategory = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
