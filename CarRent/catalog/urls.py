from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cars/', CarListView.as_view(), name='cars'),
    path('car/<slug:car_slug>/', CarDetailView.as_view(), name='car'),
    path('mycars/', LoanedCarsByUserListView.as_view(), name='my-orders'),
    path('cars_add/', cars_add, name="cars_add"),
    path('create_car/', create_car),
    path('delete_car/<int:id>/', delete_car),
    path('edit_car/<int:id>/', edit_car)
]