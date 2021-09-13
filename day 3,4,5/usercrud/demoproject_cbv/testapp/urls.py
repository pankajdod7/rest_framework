from django.urls import path
from .views import UserCBV

urlpatterns = [
    path('user/', UserCBV.as_view(), name='user'),
]
