from django import  forms


class CarsForm(forms.Form):
    title = forms.CharField(label="Марка автомобиля")
    model = forms.CharField(label="Модель автомобиля")
    reg_number = forms.CharField(label="Регистрационный номер")
