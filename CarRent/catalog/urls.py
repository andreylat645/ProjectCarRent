from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('cars/', CarListView.as_view(), name='cars'),
    path('car/<slug:car_slug>/', CarDetailView.as_view(), name='car'),
]