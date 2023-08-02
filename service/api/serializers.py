from rest_framework import serializers
from service.models import Service, Service_Employee


class Service_EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service_Employee
        fields = '__all__'        


class ServiceSerializer(serializers.ModelSerializer):
    services = Service_EmployeeSerializer(many=True, read_only=True)
    employees = Service_EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = '__all__'
