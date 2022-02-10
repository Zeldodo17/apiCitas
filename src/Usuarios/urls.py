from django.urls import path
from .views import (
    CreateUser, 
    LoginUser,
    LogoutUser,
    UpdateUser,
    DeleteUser,
    ListUsers,
    ListUser,
    )

# URLS DE LA APLICACION DE USUARIOS
urlpatterns = [
    path('auth-login/', LoginUser.as_view(), name='login'),
    path('auth-logout/', LogoutUser.as_view(), name='logout'),
    path("listUsers/", ListUsers.as_view(), name="listUsers"),
    path('listUser/<int:pk>', ListUser.as_view(), name='listUser'),
    path('createUser/', CreateUser.as_view(), name='createUser'),
    path('updateUser/<int:pk>', UpdateUser.as_view(), name='updateUser'),
    path('deleteUser/<int:pk>', DeleteUser.as_view(), name='deleteUser')
]
