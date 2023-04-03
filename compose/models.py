from constants.format import compose_string, compose_full_string
from services.models import Service


class ComposeFile:
    compose_format = compose_string
    version = ""
    services = []

    def __init__(self, version: str = "3.8", services: list[Service] = []):
        self.version = version
        self.services = services
        if (services != []):
            self.compose_format = compose_full_string
