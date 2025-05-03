from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from . models import receiveModel, itemsModel, inventoryModel
from dal import autocomplete
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class receiveForms(forms.ModelForm):
    item_data = forms.CharField(
        label='Item Name',
        max_length=100,
        help_text='Check if its added in the item list.'
    )
    quantity = forms.FloatField(
        label='Quantity',
        min_value=1,
        help_text='Value in kgs.'
    )
    received_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    class Meta:
        model = receiveModel
        fields = ['item_data', 'quantity', 'supplier', 'received_date']

class itemsForm(forms.ModelForm):

    class Meta:
        model = itemsModel
        fields = ['item_dataadd']
        


    # Add any other fields you need for the form

class InventoryForm(forms.ModelForm):
    item = forms.ModelChoiceField(
        queryset=inventoryModel.objects.all(),
        widget=autocomplete.ModelSelect2(url='inventory-autocomplete')
    )
