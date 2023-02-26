from django.shortcuts import render
from django.http import *
from .models import Car, Condition, Category, CarInstance, Status, Country, Client
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CarsForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

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

class LoanedCarsByUserListView(LoginRequiredMixin, generic.ListView):
    '''
    Класс для прелставления списка автомобилей,
    которые находятся в аренде у текущего пользователя.
    '''

    model = CarInstance
    template_name = 'catalog/carinstance_list_borrowed_user.html'
    paginate_by = 10

    def ger_queryset(self):
        return CarInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')

def cars_add(request):
    car = Car.objects.all()
    carsForm = CarsForm()
    return render(request, "catalog/cars_add.html",
                  {"form": carsForm, "car": car})

#Добавление автомобиля в бд
def create_car(request):
    if request.method == "POST":
        car = Car()
        car.title = request.POST.get("title")
        car.model = request.POST.get("model")
        car.reg_number = request.POST.get("reg_number")
        car.save()
        # Возвразаемся на предыдущую страницу
        return HttpResponseRedirect("/cars_add/")

#Удаление автомобиля
def delete_car(request, id):
    try:
        car = Car.objects.get(id=id)
        car.delete()
        return HttpResponseRedirect("/cars_add/")
    except:
        return HttpResponseNotFound("<h2> Автомобиль не найден</h2>")

#Изменение данных автомобиля
def edit_car(request, id):
    car = Car.objects.get(id=id)
    if request.method == "POST":
        car.title = request.POST.get("title")
        car.model = request.POST.get("model")
        car.reg_number = request.POST.get("reg_number")
        car.save()
        return HttpResponseRedirect("/cars_add/")
    else:
        return render(request, "catalog/edit_car.html", {"car": car})

class CarInstanceCreate(CreateView):
    model = CarInstance
    fields = "__all__"
    success_url = reverse_lazy('cars')

class CarInstanceUpdate(UpdateView):
        model = CarInstance
        fields = "__all__"
        success_url = reverse_lazy('cars')

class CarInstanceDelete(DeleteView):
    model = CarInstance
    success_url = reverse_lazy('cars')