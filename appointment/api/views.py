from rest_framework import generics
from rest_framework.generics import get_object_or_404

from appointment.api.serializers import AppointmentSerialiazer
from appointment.models import Appointment

class AppointmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerialiazer