from django.urls import path
from appointment.api import views as api_views


urlpatterns = [
    path('appointment/',api_views.AppointmentListCreateAPIView.as_view(), name='appointment-list'),
    path('appointment/<int:employee>', api_views.UserBasedAppointments.as_view(), name='user-based-app'),
]