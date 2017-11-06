from django.apps import AppConfig


class RavenConfig(AppConfig):
    name = 'raven'
    verbose_name = 'Raven'

    def ready(self):
        from .client import DjangoClient  # NOQA

