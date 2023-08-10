from django.db import models
from employee.models import Employee

# Create your models here.
class Service(models.Model):
    service_name = models.CharField(max_length=150)
    duration = models.IntegerField()
    default_price = models.FloatField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_name


class Service_Employee(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='services')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employees')
    price = models.FloatField()
    duration = models.IntegerField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.price}'
