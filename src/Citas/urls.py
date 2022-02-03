from django.urls import path
from .views import createDate

urlpatterns = [
    path('createDate/', createDate.as_view())
]
