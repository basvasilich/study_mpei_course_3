from django.contrib import admin

from .models import Vehicle, VehicleModel, Order, Employee, EmployeeRole, Route, Depot, Location

# Register your models here.
admin.site.register(Employee)
admin.site.register(EmployeeRole)
admin.site.register(VehicleModel)
admin.site.register(Vehicle)
admin.site.register(Depot)
admin.site.register(Order)
admin.site.register(Route)
admin.site.register(Location)
