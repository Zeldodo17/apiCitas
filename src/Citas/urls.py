from django.urls import path
from .views import crudDate,UpdateDate

urlpatterns = [
    path('createDate/', crudDate.as_view(), name='createDate'),
    path('updateDate/<int:pk>', UpdateDate.as_view(), name='updateDate'),
]
