from django.urls import path
from core import views


urlpatterns = [
    path('', views.drinks, name='Get All Drinks'),
    path('<int:drink_id>/', views.drink_by_id, name='Get Drink by ID'),
]