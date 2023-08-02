from django.contrib import admin
from employee.models import Employee, Employee_Rating, Employee_Working_Day_Time

# Register your models here.
admin.site.register(Employee)
admin.site.register(Employee_Rating)
admin.site.register(Employee_Working_Day_Time)
