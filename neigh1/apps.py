from django.apps import AppConfig


class Neigh1Config(AppConfig):
    name = 'neigh1'
    def ready(self):
        import neigh1.signals
