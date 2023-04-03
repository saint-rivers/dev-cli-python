from app.constants.format import compose_string, compose_full_string
from app.services.models import Service, Formattable


class ComposeFile:
    compose_format = compose_string
    version = ""
    services = []

    def __init__(self, version: str = "3.8", services: list[Formattable] = []):
        self.version = version
        self.services = services
        if (services != []):
            self.compose_format = compose_full_string
