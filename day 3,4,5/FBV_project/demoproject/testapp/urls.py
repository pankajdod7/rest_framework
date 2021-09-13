from django.urls import path
from .views import employeedetail

urlpatterns = [
    path('emp/', employeedetail),
]