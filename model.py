from format import compose_string, compose_full_string, service_string
from mapper import map_dict_to_string


class EnvironmentVariables:
    values = {}

    def __init__(self, map={}):
        for k, v in map.items():
            self.values[k] = v


class Formattable:
    name = "sample-service"
    container_name = "sample-service"
    environment_variables: EnvironmentVariables = None
    ports = []

    def __init__(self,
                 name: str = "sample-service",
                 container_name: str = "sample-service",
                 variables={},
                 ports=[]
                 ):
        self.name = name
        self.container_name = container_name
        self.environment_variables = EnvironmentVariables(variables)
        self.ports = ports

    def to_string(self) -> str:
        pass


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

    def to_string(self) -> str:
        output = service_string
        output = output.replace("**service-name**", self.name)
        output = output.replace("**context**", self.context)
        output = output.replace("**dockerfile**", self.dockerfile)
        output = output.replace("**container-name**", self.container_name)
        output = output.replace(
            "**environment**", map_dict_to_string(self.environment_variables.values))
        return output


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

    def to_string(self) -> str:
        output = service_string
        output = output.replace("**service-name**", self.name)
        output = output.replace("**image**", self.image)
        output = output.replace("**version**", self.version)
        output = output.replace("**container-name**", self.container_name)
        output = output.replace(
            "**environment**", map_dict_to_string(self.environment_variables.values))
        return output


class ComposeFile:
    compose_format = compose_string
    version = ""
    services = []

    def __init__(self, version: str = "3.8", services=[]):
        self.version = version
        self.services = services
        if (services != []):
            self.compose_format = compose_full_string
