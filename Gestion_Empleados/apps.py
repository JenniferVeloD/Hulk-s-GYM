from django.apps import AppConfig


class GestionEmpleadosConfig(AppConfig):
    """
    Define metadatos y configuraciones para la aplicación "Gestion_Empleados"
    """
    default_auto_field = "django.db.models.BigAutoField"
    """
    Campo que Django usa para las claves primarias de los modelos de la aplicacion
    """
    name = "Gestion_Empleados"
    """
    Define el nombre de la aplicación
    """
