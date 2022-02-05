from django.urls import path
from .views import (
    listDates,
    listDate,
    createDate,
    updateDate,
    deleteDate
    )

urlpatterns = [
    path('listDates/', listDates.as_view()),
    path('listDate/<int:pk>', listDate.as_view()),
    path('createDate/', createDate.as_view(), name='createDate'),
    path('updateDate/<int:pk>', updateDate.as_view(), name='updateDate'),
    path('deleteDate/<int:pk>', deleteDate.as_view(), name='deleteDate')
]
