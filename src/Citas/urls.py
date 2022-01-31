from django.urls import path
from .views import Hola

urlpatterns = [
    path('hola/', Hola.as_view(), name='hola'),
]
