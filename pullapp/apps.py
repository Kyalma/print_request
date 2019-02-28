from django.apps import AppConfig


class PullappConfig(AppConfig):
    name = 'pullapp'

    def ready(self):
        import pullapp.signals
