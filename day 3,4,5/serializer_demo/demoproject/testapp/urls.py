from django.urls import path
from .views import StudentDetails

urlpatterns = [
    path('student/', StudentDetails.as_view()),
]
