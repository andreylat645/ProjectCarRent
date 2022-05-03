from django.shortcuts import render
from .models import Car, Condition, Category, CarInstance, Status, Country, Client
from django.http import HttpResponse
from django.views import generic


def index(request):
    num_car = Car.objects.all().count()
    num_instance = CarInstance.objects.all().count()

    # Доступные автомобили
    num_instance_available = CarInstance.objects.filter(status__exact=2).count()

    # Количество посещений этого view
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request, 'index.html',
                  context={'num_car': num_car,
                           'num_instance': num_instance,
                           'num_instance_available': num_instance_available,
                           'num_visits': num_visits}
                  )


class CarListView(generic.ListView):
    model = Car
    paginate_by = 3

class CarDetailView(generic.DetailView):
    model = Car
    slug_url_kwarg = 'car_slug'
    context_object_name = 'car'

