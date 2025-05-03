import django_tables2 as tables
from .models import inventoryModel

class InventoryTable(tables.Table):
    class Meta:
        model = inventoryModel
        template_name = "django_tables2/bootstrap.html"



