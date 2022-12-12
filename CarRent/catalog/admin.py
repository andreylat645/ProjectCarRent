from django.contrib import admin
from .models import Car, Condition, Category, CarInstance, Status, Country, Client

admin.site.register(Car)
admin.site.register(Condition)
admin.site.register(Category)
# admin.site.register(CarInstance)
admin.site.register(Status)
admin.site.register(Country)
admin.site.register(Client)


@admin.register(CarInstance)
class CarInstanceAdmin(admin.ModelAdmin):
    list_display = ["car", "status", "date_start", "borrower", "date_back", "client"]
    list_filter = ["car","status"]

    fieldsets = (
        ('Автомобиль и клиент', {
            'fields': ('car', 'client')
        }),
        ('Статус и сроки аренды', {
            'fields' : ('status', 'date_start', 'date_back', 'borrower')
        })
    )