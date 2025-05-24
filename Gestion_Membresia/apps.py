from django.apps import AppConfig


class GestionMembresiaConfig(AppConfig):
    """
    Define metadatos y configuraciones para la aplicación "Gestion_Membresia"
    """
    default_auto_field = "django.db.models.BigAutoField"
    """
    Campo que Django usa para las claves primarias de los modelos de la aplicacion
    """
    name = "Gestion_Membresia"
    """
    Define el nombre de la aplicación
    """
