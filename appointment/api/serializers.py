from rest_framework import serializers
from appointment.models import Appointment


class AppointmentSerialiazer(serializers.ModelSerializer):
    
    class Meta:
        model = Appointment
        fields = '__all__'
        