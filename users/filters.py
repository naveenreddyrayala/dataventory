from .models import inventoryModel
import django_filters

class InventoryFilter(django_filters.FilterSet):
    item = django_filters.CharFilter(lookup_expr='icontains')  # Enables text search

    class Meta:
        model = inventoryModel
        fields = ['item']