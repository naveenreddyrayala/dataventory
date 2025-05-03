from django.contrib import admin
from . models import receiveModel, itemsModel, inventoryModel

admin.site.register(receiveModel)
admin.site.register(itemsModel)
admin.site.register(inventoryModel)