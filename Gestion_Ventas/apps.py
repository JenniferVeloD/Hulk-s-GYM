from django.apps import AppConfig


class GestionVentasConfig(AppConfig):
    """
    Define metadatos y configuraciones para la aplicación "Gestion_Ventas"
    """
    default_auto_field = "django.db.models.BigAutoField"
    """
    Campo que Django usa para las claves primarias de los modelos de la aplicacion
    """
    name = "Gestion_Ventas"
    """
    Define el nombre de la aplicación
    """

