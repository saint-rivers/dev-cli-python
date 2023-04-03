import app.file.file as file
from app.constants.format import *


def write_dockerfile(dockerfile: str):
    switch = {
        'jre': jre_string,
        'keycloak': keycloak_string
    }
    dockerfile_content = switch.get(
        dockerfile, "specified dockerfile not available")

    file.write_to_dockerfile(dockerfile_content)
