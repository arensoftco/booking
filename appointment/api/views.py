from rest_framework import generics
from rest_framework.generics import get_object_or_404

from appointment.api.serializers import AppointmentSerialiazer
from appointment.models import Appointment

class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerialiazer

class UserBasedAppointments(generics.ListCreateAPIView):
    # queryset = Appointment.objects.all()
    serializer_class = AppointmentSerialiazer

    def get_queryset(self):
        employee_pk = self.kwargs['employee']
        print(employee_pk)
        return Appointment.objects.filter(employee=employee_pk)
    
    def perform_create(self, serializer):
        employee_pk = self.kwargs['employee']
        employee = get_object_or_404(Appointment, employee=employee_pk)
        serializer.save(employee=employee)