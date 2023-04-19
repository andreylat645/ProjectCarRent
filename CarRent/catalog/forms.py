from django import  forms
import datetime
from django.forms import ModelForm
from .models import CarInstance, Car, Client, Status

class CarsForm(forms.Form):
    title = forms.CharField(label="Марка автомобиля")
    model = forms.CharField(label="Модель автомобиля")
    reg_number = forms.CharField(label="Регистрационный номер")

class InstancesForm(forms.Form):
    car = forms.ModelChoiceField(label="Автомобиль", queryset=Car.objects.all())
    status = forms.ModelChoiceField(label="Статус", queryset=Status.objects.all())
    date_start = forms.DateField(label="Дата нач.аренды", widget=forms.SelectDateWidget, initial=datetime.date.today)
    date_back = forms.CharField(label="Дата завер.аренды", widget=forms.SelectDateWidget, initial=datetime.date.today)
    client = forms.ModelChoiceField(label="Клиент", queryset=Client.objects.all())

# class CarInstanceModelForm(forms.Form):
#     class Meta:
#         model = CarInstance
#         fields = ['car', 'status', 'date_start', 'date_back', 'client']