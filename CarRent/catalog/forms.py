from django import  forms
from django.forms import ModelForm
from .models import CarInstance

class CarsForm(forms.Form):
    title = forms.CharField(label="Марка автомобиля")
    model = forms.CharField(label="Модель автомобиля")
    reg_number = forms.CharField(label="Регистрационный номер")

class CarInstanceModelForm(forms.Form):
    class Meta:
        model = CarInstance
        fields = ['car', 'status', 'date_start', 'date_back', 'client']