from django.apps import AppConfig


class InicioSesionConfig(AppConfig):
    """
    Define metadatos y configuraciones para la aplicación "Inicio_Sesion"
    """
    default_auto_field = "django.db.models.BigAutoField"
    """
    Campo que Django usa para las claves primarias de los modelos de la aplicacion
    """
    name = "Inicio_Sesion"
    """
    Define el nombre de la aplicación
    """
