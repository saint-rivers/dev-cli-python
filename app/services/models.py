import app.constants.format as format


class EnvironmentVariables:
    values = {}

    def __init__(self, map={}):
        for k, v in map.items():
            self.values[k] = v


class PortMapping:
    host_port = ""
    container_port = ""

    def __init__(self, host_port: str, container_port: str):
        self.host_port = host_port
        self.container_port = container_port


class Formattable:
    name = "sample-service"
    container_name = "sample-service"
    env: dict[str, str] = None
    ports = list[PortMapping]

    def __init__(self,
                 variables: dict[str, str] = {},
                 name: str = "sample-service",
                 container_name: str = "sample-service",
                 ports: list[PortMapping] = []
                 ):
        self.name = name
        self.container_name = container_name
        self.env = variables
        self.ports = ports


class FromDockerfile(Formattable):
    dockerfile = ""
    context = ""

    def __init__(self,
                 context: str = ".",
                 dockerfile: str = "Dockerfile",
                 variables: dict[str, str] = {},
                 name: str = "sample-service",
                 container_name: str = "sample-service",
                 ports: list[PortMapping] = []
                 ):
        super().__init__(name=name,
                         container_name=container_name,
                         variables=variables,
                         ports=ports
                         )
        self.context = context
        self.dockerfile = dockerfile


class Service(Formattable):
    name = "sample-service"
    container_name = "sample-service"

    def __init__(self,
                 image: str,
                 image_version: str,
                 variables: dict[str, str] = {},
                 name: str = "sample-service",
                 container_name: str = "sample-service",
                 ports: list[PortMapping] = []
                 ):
        super().__init__(name=name,
                         container_name=container_name,
                         variables=variables,
                         ports=ports
                         )
        self.image = image
        self.version = image_version
