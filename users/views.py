from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate
from . forms import UserRegisterForm, receiveForms, itemsForm
from django.contrib import messages
from . models import receiveModel, itemsModel, inventoryModel
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django_tables2 import SingleTableView
from .tables import InventoryTable
from .filters import InventoryFilter


def home(request):
    return render(request, 'users/home.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, "Welcome back, {username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'users/login.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account created for {username}!")
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})

def profile(request):
    return render(request, 'users/profile.html')

def about(request):
    return render(request, 'users/about.html')

def services(request):
    return render(request, 'users/services.html')
# Create your views here.

def receives(request):
    if request.method == 'POST':
        form = receiveForms(request.POST)
        items = request.POST.get('item_data')
        if itemsModel.objects.filter(item_dataadd=items).exists():
            if form.is_valid():
                form.save()
                instance = form.save()  # Save the data to the database
                messages.success(request, "Items added successfully!")
                try:
                    inventory = inventoryModel.objects.get(item=instance.item_data)
                    inventory.qty += instance.quantity  # Assuming instance has this field,
                    inventory.save()
                except ObjectDoesNotExist:
                    inventoryModel.objects.create(
                            item=instance.item_data,
                            qty=instance.quantity,
                            ) 
        else:  
            messages.error(request, "Error does not exisits need to add!")
            return redirect('itemsadd')
    else:
        form = receiveForms()

    return render(request, 'users/receives.html', {'form': form})

def display(request):
    data = receiveModel.objects.all() 
    return render(request, 'users/display.html', {'data': data})

def itemsadd(request):
    if request.method == 'POST':
        form = itemsForm(request.POST)
        items = request.POST.get('item_dataadd')  # Get the username from the form
        if itemsModel.objects.filter(item_dataadd=items).exists():
            messages.error(request, "Error items Exits dont need to add!")
            return redirect('itemsadd')
        elif form.is_valid():
             form.save()
             messages.success(request, "Items added successfully!")
        return redirect('itemsadd')
    else:
        form = itemsForm()

    return render(request, 'users/items.html', {'form': form})

def inventory(request):
    data = inventoryModel.objects.all() 
    return render(request, 'users/inventory.html', {'data': data})

def itemslist(request):
    data = itemsModel.objects.all() 
    return render(request, 'users/listitems.html', {'data': data})

#def search(request):
 #   return render(request, 'users/search.html')

class InventoryAutocomplete(View):
    def get(self, request):
        query = request.GET.get('term', '')
        items = inventoryModel.objects.filter(item__icontains=query)[:10]
        results = [inventory.item for inventory in items]
        return JsonResponse(results, safe=False)
    
class InventoryListView(SingleTableView):
    model = inventoryModel
    table_class = InventoryTable
    template_name = "users/inventory_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = InventoryFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = self.filterset
        return context
