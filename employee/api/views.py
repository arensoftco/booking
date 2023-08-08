from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
from employee.api.permissions import IsAdminOrReadOnly
from rest_framework.response import Response

from employee.api.serializers import EmployeeSerializer, Employee_RatingSerializer, Employee_Working_Day_TimeSerializer
from employee.models import Employee, Employee_Rating, Employee_Working_Day_Time


class EmployeeListCreateAPIView(generics.ListCreateAPIView):
    # permission_classes = [IsAdminOrReadOnly]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAdminUser]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class Employee_RatingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee_Rating.objects.all()
    serializer_class = Employee_RatingSerializer

    def retrieve(self, request, *args, **kwargs):
        employee_pk = self.kwargs.get('employee_pk')
        rating_pk = self.kwargs.get('pk')
        rating = get_object_or_404(Employee_Rating, employee=employee_pk, id=rating_pk)
        serializer = self.get_serializer(rating)
        return Response(serializer.data)


class Employee_RatingCreateAPIView(generics.ListCreateAPIView):
    queryset = Employee_Rating.objects.all()
    serializer_class = Employee_RatingSerializer

    """ 
    Only list employee's ratings
     """
    def get_queryset(self):
        employee_pk = self.kwargs['employee_pk']
        print(employee_pk)
        return Employee_Rating.objects.filter(employee=employee_pk)
    
    def perform_create(self, serializer):
        employee_pk = self.kwargs.get('employee_pk')
        employee = get_object_or_404(Employee, pk=employee_pk)

        serializer.save(employee=employee)


class Employee_Working_Day_TimeAPIView(generics.ListCreateAPIView):
    queryset = Employee_Working_Day_Time.objects.all()
    serializer_class = Employee_Working_Day_TimeSerializer

    def get_queryset(self):
        employee_pk = self.kwargs['employee_pk']
        return Employee_Working_Day_Time.objects.filter(employee=employee_pk)

    def perform_create(self, serializer):
        employee_pk = self.kwargs.get('employee_pk')
        employee = get_object_or_404(Employee, pk=employee_pk)

        serializer.save(employee=employee)


class Employee_Working_Day_TimeDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee_Working_Day_Time.objects.all()
    serializer_class = Employee_Working_Day_TimeSerializer

    def retrieve(self, request, *args, **kwargs):
        employee_pk = self.kwargs.get('employee_pk')
        wdt_pk = self.kwargs.get('pk')
        wdt = get_object_or_404(Employee_Working_Day_Time, employee=employee_pk, id = wdt_pk)
        serializer = self.get_serializer(wdt)
        return super().retrieve(serializer.data)