from app.constants.format import *


def write_to_compose_file(content: str):
    with open('docker-compose.yml', 'w') as compose:
        compose.write(content)


def write_to_dockerfile(content: str):
    with open('Dockerfile', 'w') as file:
        file.write(content)
