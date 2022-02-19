from django.urls import path
from .views import(
        listTasks,
        createTask,
        updateTask,
        deleteTask,
    )

urlpatterns = [
    path('listTasks/<str:mascota>', listTasks.as_view()),
    path('createTask/', createTask.as_view()),
    path('updateTask/<int:pk>', updateTask.as_view()),
    path('deleteTask/<int:pk>', deleteTask.as_view())
]
