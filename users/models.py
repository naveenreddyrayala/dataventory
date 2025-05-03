from django.db import models
import django_tables2 as tables

# Create your models here.

class receiveModel(models.Model):
    item_data = models.CharField(max_length=100)
    quantity = models.FloatField()
    supplier = models.CharField(max_length=100)
    received_date = models.DateField()
    
class itemsModel(models.Model):
    item_dataadd = models.CharField(max_length=100)

class inventoryModel(models.Model):
    item = models.CharField(max_length=100)
    qty = models.IntegerField()

    def __str__(self):
        return self.item
    





