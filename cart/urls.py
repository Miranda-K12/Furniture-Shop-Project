from django.urls import path
from .views import get_cart, add_to_cart, remove_from_cart

urlpatterns = [
    path('<int:id>/', get_cart, name='cart-detail'),
    path('add/', add_to_cart, name='cart-add'),
    path('remove/', remove_from_cart, name='cart-remove'),
]