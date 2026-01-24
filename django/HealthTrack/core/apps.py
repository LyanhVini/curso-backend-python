from django.apps import AppConfig
from django.db.models.signals import post_migrate

def criar_grupos_iniciais(sender, **kwargs):
    from django.contrib.auth.models import Group
    Group.objects.get_or_create(name="Paciente")
    Group.objects.get_or_create(name="Medico")

class CoreConfig(AppConfig):
    name = 'core'
    default_auto_field = 'django.db.models.BigAutoField'

    def ready(self):
        post_migrate.connect(criar_grupos_iniciais, sender=self)
