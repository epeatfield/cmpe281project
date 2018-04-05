from django.apps import AppConfig


class WaterWatchApiConfig(AppConfig):
    name = 'water_watch_api'

    def ready(self):
        from . import signals
