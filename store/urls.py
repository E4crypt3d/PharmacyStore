from django.urls import path
from store import views


urlpatterns = [
    path('', views.home, name='home'),
    path('sales', views.sales, name='sales'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('sales/sort', views.sort_products, name='sort'),
]
