from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import InventoryAutocomplete, InventoryListView

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('home/', views.home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('receives/', views.receives, name='receives'),
    path('display/', views.display, name='display'),
    path('items/', views.itemsadd, name='itemsadd'),
    path('inventory/', views.inventory, name='inventory'),
    path('listitems/', views.itemslist, name='itemslist'),
    #path('search/', views.search, name='search'),
    path('search/', InventoryAutocomplete.as_view(), name='inventory_autocomplete'),
    path('inventory_list/', InventoryListView.as_view(), name='inventory_list'),
]