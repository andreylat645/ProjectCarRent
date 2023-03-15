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
    path('edit_car/<int:id>/', edit_car),
    path('instances_add/', instances_add, name="instances_add")
    # path('carinstance/create/', CarInstanceCreate.as_view(), name="car_instance_create"),
    # path('carinstances/update/<slug:slug>/', CarInstanceUpdate.as_view(), name="car_instance_update"),
    # path('carinstances/delete/<slug:slug>/', CarInstanceDelete.as_view(), name="car_instance_delete")
]