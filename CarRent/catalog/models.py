import uuid

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

@property
def is_overdue(self):
    if self.due_back and date.today() > self.due_back:
        return True
    return False


class Category(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите категорию автомобиля",
                            verbose_name="Категория автомобиля")

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField(max_length=30,
                                  help_text="Введите имя клиента",
                                  verbose_name="Имя клиента")
    last_name = models.CharField(max_length=30,
                                 help_text="Введите фамилию клиента",
                                 verbose_name="Фамилия клиента")

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Condition(models.Model):
    name = models.CharField(max_length=50,
                            help_text="Введите состояние автомобиля",
                            verbose_name="Состояние автомобиля")

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=50,
                            help_text="Введите страну производителя",
                            verbose_name="Страна производителя")

    class Meta:
        verbose_name_plural = "country"

    def __str__(self):
        return self.name


class Car(models.Model):
    title = models.CharField(max_length=50,
                             null=True,
                             help_text="Введите марку автомобиля",
                             verbose_name="Марка автомобиля")
    slug = models.SlugField(max_length=255,
                            unique=True,
                            db_index=True,
                            verbose_name="URL",
                            default=uuid.uuid1)
    model = models.CharField(max_length=50,
                             null=True,
                             help_text="Введите модель автомобиля",
                             verbose_name="Модель автомобиля")
    num = models.CharField(max_length=20, null=True,
                           help_text="Введите номер автомобиля в автопарке",
                           verbose_name="Номер автомобиля в парке")
    reg_number = models.CharField(max_length=20,
                                  help_text="Введите рег.номер автомобиля",
                                  verbose_name="Рег.номер автомобиля")
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 null=True,
                                 help_text="Выберите категорию автомобиля",
                                 verbose_name="Категория автомобиля")
    country = models.ForeignKey('Country',
                                on_delete=models.CASCADE,
                                null=True,
                                help_text="Выберите страну производства",
                                verbose_name="Страна производства")
    condition = models.ForeignKey('Condition',
                                  on_delete=models.CASCADE,
                                  null=True,
                                  help_text="Выберите состояние автомобиля",
                                  verbose_name="Состояние автомобиля")

    def get_absolute_url(self):
        return reverse('car', kwargs={'car_slug': self.slug})

    def __str__(self):
        return '%s %s %s' % (self.num, self.title, self.model)

    class Meta:
        ordering = ["num"]


class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_text="Введите статус автомобиля",
                            verbose_name="Статус автомобиля")

    class Meta:
        verbose_name_plural = "statuses"

    def __str__(self):
        return self.name


class CarInstance(models.Model):
    car = models.ForeignKey('Car',
                            on_delete=models.CASCADE,
                            null=True,
                            verbose_name="Автомобиль")
    status = models.ForeignKey('Status', on_delete=models.CASCADE,
                               null=False,
                               help_text="Изменить статус автомобиля",
                               verbose_name="Статус автомобиля")
    date_start = models.DateField(null=True, blank=True,
                                  help_text="Введите начало срока аренды",
                                  verbose_name="Дата начала статуса")
    date_back = models.DateField(null=True, blank=True,
                                 help_text="Введите конец срока аренды",
                                 verbose_name="Дата окончания статуса")
    client = models.ForeignKey('Client', on_delete=models.CASCADE,
                               null=True,
                               help_text="Выберите клиента",
                               verbose_name="Клиент")
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null=True, blank=True,
                                 verbose_name="Заказчик",
                                 help_text="Выберите клиента заказа")

    class Meta:
        ordering = ["date_back"]

    @property
    def is_overdue(self):
        if self.date_back and date.today() > self.date_back:
            return True
        return False

    def __str__(self):
        return '%s %s' % (self.car, self.status)
