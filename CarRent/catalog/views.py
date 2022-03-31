from django.shortcuts import render
from .models import Car, Condition, Category, CarInstance, Status, Country, Client
from django.http import HttpResponse

def index(request):
    num_car = Car.objects.all().count()
    num_instance = CarInstance.objects.all().count()

    # Доступные автомобили
    num_instance_available = CarInstance.objects.filter(status__exact=2).count()

    return render(request, 'index.html',
                  context={'num_car': num_car,
                           'num_instance': num_instance,
                           'num_instance_available': num_instance_available},
                  )