from app.compose.models import ComposeFile
from app.services.models import Service, PortMapping, FromDockerfile

keycloak_compose = ComposeFile(
    version="3.8",
    services=[
        FromDockerfile(
            ports=[PortMapping("8800", "8080"), PortMapping("8443", "8443")]
        )
    ],
)
