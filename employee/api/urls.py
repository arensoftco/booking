from django.urls import path
from employee.api import views as api_views


urlpatterns = [
    path('employee/',api_views.EmployeeListCreateAPIView.as_view(), name='employee-list'),
    path('employee/<int:pk>', api_views.EmployeeDetailAPIView.as_view(), name='employee-details'),
    path('employee/<int:employee_pk>/rating', api_views.Employee_RatingCreateAPIView.as_view(), name='employee-ratings'),
    path('employee/<int:employee_pk>/rating/<int:pk>', api_views.Employee_RatingDetailAPIView.as_view(), name='rating'),
    path('employee/<int:employee_pk>/workdaytime', api_views.Employee_Working_Day_TimeAPIView.as_view(), name='employee-work-day-time'),
    path('employee/<int:employee_pk>/workdaytime/<int:pk>', api_views.Employee_Working_Day_TimeDetailAPIView.as_view(), name='work-day-times'),
]