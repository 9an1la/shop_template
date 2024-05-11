import django_filters
from django import forms

from apps.shop.models import Product

CHOICES_MANUFACTURER = [(i['manufacturer'], i['manufacturer']) for i in Product.objects.values().order_by('manufacturer').distinct('manufacturer')]


class ProductFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    manufacturer = django_filters.MultipleChoiceFilter(
        field_name='manufacturer',
        widget=forms.CheckboxSelectMultiple,
        choices=CHOICES_MANUFACTURER
    )

    title = django_filters.ModelMultipleChoiceFilter(
        field_name='title',
        to_field_name='title',
        queryset=Product.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Model:'
    )

    class Meta:
        model = Product
        fields = ['manufacturer', 'title']
