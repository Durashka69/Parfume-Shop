from django_filters import rest_framework as filters
from main.models import Product


class ProductFilter(filters.FilterSet):
    price_from = filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_to = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['brand', 'volume', 'family', 'for_men', 'notes', 'price_from', 'price_to']
