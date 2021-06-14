from django.db import models


class EmployeeRole(models.Model):
    title = models.CharField(max_length=200, help_text='Название')

    class Meta:
        verbose_name = "Роль"
        verbose_name_plural = "Роли"

    def __str__(self):
        return self.title


class Employee(models.Model):
    start_date = models.DateField(auto_now_add=True, blank=True)
    name = models.CharField(max_length=200, help_text='Имя')
    surname = models.CharField(max_length=200, help_text='Фамилия')
    phone = models.CharField(max_length=14, help_text='Номер телефона')
    role_id = models.ForeignKey(EmployeeRole, on_delete=models.DO_NOTHING, help_text='Роль')

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return self.name + ' ' + self.surname


class VehicleModel(models.Model):
    volume = models.FloatField(help_text='Объем кузова')
    capacity = models.FloatField(help_text='Грузоподъемность')
    title = models.CharField(max_length=200, help_text='Название модели')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Модель ТС"
        verbose_name_plural = "Модели ТС"



class Vehicle(models.Model):
    model_id = models.ForeignKey(VehicleModel, on_delete=models.DO_NOTHING, help_text='Модель машины')
    number = models.CharField(max_length=200, help_text='Госномер', primary_key=True)

    def __str__(self):
        return self.number


    class Meta:
        verbose_name = "Транспортное средство"
        verbose_name_plural = "Транспортные средства"


class Location(models.Model):
    lat = models.FloatField(help_text='Широта')
    lon = models.FloatField(help_text='Долгота')
    address = models.CharField(max_length=200, blank=True, help_text='Адрес')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"




class Order(models.Model):
    location_id = models.ForeignKey(Location, on_delete=models.DO_NOTHING, help_text='Адрес заказа')
    volume = models.FloatField(help_text='Объем заказа')
    capacity = models.FloatField(help_text='Вес заказа')
    title = models.CharField(max_length=200, help_text='Комментарий к заказу')
    phone = models.CharField(max_length=14, help_text='Номер телефона получателя')
    isDelivered = models.BooleanField(default=False, help_text='Заказ доставлен')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.title




class Depot(models.Model):
    location_id = models.ForeignKey(Location, on_delete=models.DO_NOTHING, help_text='Адрес склада')
    title = models.CharField(max_length=200, help_text='Название склада')

    class Meta:
        verbose_name = "Склад"
        verbose_name_plural = "Склады"

    def __str__(self):
        return self.title


class Route(models.Model):
    vehicle_number = models.ForeignKey(Vehicle, on_delete=models.DO_NOTHING, help_text='Машина')
    orders = models.ManyToManyField(Order)
    depots = models.ManyToManyField(Depot)
    courier = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, help_text='Курьер', related_name='+')
    logistician = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, help_text='Логист', related_name='+')
    title = models.CharField(blank=True, max_length=200, help_text='Комментарий к маршруту')
    date = models.DateField(blank=False, help_text='Дата маршрута')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Маршрут"
        verbose_name_plural = "Маршруты"