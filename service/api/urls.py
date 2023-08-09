from django.urls import path
from service.api import views as api_views


urlpatterns = [
    path('service/',api_views.ServiceListCreateAPIView.as_view(), name='service-list'),
    path('service/<int:pk>',api_views.ServiceDetailAPIView.as_view(), name='service-detail'),
    path('service/<int:service_pk>/employee',api_views.ServiceEmployeeListCreateAPIView.as_view(), name='service-employee'),
    path('service/employee/<int:employee_pk>',api_views.EmployeeListOfService.as_view(), name='employee-list-of-service')
]