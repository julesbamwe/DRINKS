from django.urls import path
from core import views


urlpatterns = [
    path('', views.get_all_drinks, name='Get All Drinks'),
    path('<int:drink_id>/', views.get_drink_by_id, name='Get Drink by ID'),
]