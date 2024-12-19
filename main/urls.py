from .views import index, contacts, services
from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('contacts/', contacts, name="contacts"),
    path('services/', services, name="services")
]
