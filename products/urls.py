from django.urls import path
from . import views

app_name= 'products'

urlpatterns = [
    path('product/', views.product_list),
    path('product/<int:pk>/', views.product_detail),
]