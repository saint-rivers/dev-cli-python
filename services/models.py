import format as format


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
    env: EnvironmentVariables = None
    ports = []

    def __init__(self,
                 name: str = "sample-service",
                 container_name: str = "sample-service",
                 variables={},
                 ports=[]
                 ):
        self.name = name
        self.container_name = container_name
        self.env = EnvironmentVariables(variables)
        self.ports = ports


class Dockerfile(Formattable):
    dockerfile = ""
    context = ""

    def __init__(self,
                 context: str = ".",
                 dockerfile: str = "Dockerfile",
                 variables={},
                 name: str = "sample-service",
                 container_name: str = "sample-service",
                 ports=[]
                 ):
        super().__init__(name, container_name, variables, ports)
        self.context = context
        self.dockerfile = dockerfile


class Service(Formattable):
    name = "sample-service"
    container_name = "sample-service"

    def __init__(self,
                 image: str,
                 image_version: str,
                 variables={},
                 name: str = "sample-service",
                 container_name: str = "sample-service",
                 ports=[]
                 ):
        super().__init__(name, container_name, variables, ports)
        self.image = image
        self.version = image_version
