from django.urls import path
from .views import hotel_list, hotel_detail

urlpatterns = [
    path('hotels/', hotel_list),
    path('detail/<int:pk>/', hotel_detail),
]