from django.urls import path
from .views import OrderListAPIView, OrderDetailAPIView, create_order

urlpatterns = [
    path('', OrderListAPIView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetailAPIView.as_view(), name='order-detail'),
    path('create/', create_order, name='order-create'),
]