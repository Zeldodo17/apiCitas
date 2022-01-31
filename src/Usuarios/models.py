from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# AQUI MODIFICAMOS EL MODELO DE USUARIOS QUE TRAE POR DEFECTO DJANGO
class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombres, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo!')

        usuario = self.model(
            username=username,
            email=self.normalize_email(email),
            nombres=nombres
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, username, email, nombres, password):
        usuario = self.create_user(
            email,
            username=username,
            nombres=nombres,
            password=password
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

# ESTE ES EL MODELO DE USUARIOS DE LA APLICACION
class Usuarios(AbstractBaseUser):
    nombres = models.CharField("Nombre", max_length=70)
    username = models.CharField("Nombre de usuario", max_length=50, unique=True)
    email = models.EmailField("Correo Electronico", max_length=254, unique=True)
    telefono = models.CharField("Numero de telefono", max_length=10, null=False, blank=False, unique=True)
    usuario_administrador = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombres', 'email']

    def __str__(self):
        return "{}".format(self.nombres)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'