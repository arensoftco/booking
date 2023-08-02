from django.db import models
from employee.models import Employee
from service.models import Service


class Appointment(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='app_services')
    employee = models.ForeignKey(Employee, on_delete=models.SET(1), related_name='app_pythemployees')

    appointment_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    duration = models.SmallIntegerField()
    description = models.TextField(blank=True, null=True)
    color_code = models.CharField(max_length=7, default='CCCCCC')
    done = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.employee}, {self.service}'
