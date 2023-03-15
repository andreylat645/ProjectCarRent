from django import  forms
from django.forms import ModelForm
from .models import CarInstance

class CarsForm(forms.Form):
    title = forms.CharField(label="Марка автомобиля")
    model = forms.CharField(label="Модель автомобиля")
    reg_number = forms.CharField(label="Регистрационный номер")

class InstancesForm(forms.Form):
    car = forms.CharField(label="Автомобиль")
    status = forms.CharField(label="Статус")
    date_start = forms.CharField(label="Дата нач.аренды")
    date_back = forms.CharField(label="Дата завер.аренды")
    client = forms.CharField(label="Клиент")

# class CarInstanceModelForm(forms.Form):
#     class Meta:
#         model = CarInstance
#         fields = ['car', 'status', 'date_start', 'date_back', 'client']