from django.apps import AppConfig


class ProyectoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Aplicaciones.proyecto'

class ProyectosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "Aplicaciones.contacto"

class ContactoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contacto'
