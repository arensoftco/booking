from rest_framework import serializers
from employee.models import Employee, Employee_Rating, Employee_Working_Day_Time


class Employee_RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Rating
        fields = '__all__' 
        # exclude = ['employee']


class Employee_Working_Day_TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee_Working_Day_Time
        # fields = '__all__'        
        exclude = ['employee']


class EmployeeSerializer(serializers.ModelSerializer):
    ratings = Employee_RatingSerializer(many=True, read_only=True)
    working_days_times = Employee_Working_Day_TimeSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'

