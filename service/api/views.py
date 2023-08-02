from rest_framework import generics
from rest_framework.generics import get_object_or_404

from service.api.serializers import Service_EmployeeSerializer, ServiceSerializer
from service.models import Service, Service_Employee


class ServiceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ServiceEmployeeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Service_Employee.objects.all()
    serializer_class = Service_EmployeeSerializer

    def get_queryset(self):
        service_pk = self.kwargs['service_pk']
        print(service_pk)
        return Service_Employee.objects.filter(service=service_pk)
    
    def perform_create(self, serializer):
        service_pk = self.kwargs.get('service_pk')
        print (f'perform create {service_pk}')
        employee = get_object_or_404(Service, pk=service_pk)

        serializer.save(service=employee)