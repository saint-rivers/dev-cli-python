from dataclasses import dataclass
from format import compose_string, compose_full_string, service_string
from mapper import map_dict_to_string


# class DatabaseEnvironment:
#     database = ""
#     username = ""
#     password = ""

#     def __init__(self, database="default", username="postgres", password="password"):
#         self.database = database
#         self.username = username
#         self.password = password

#     def to_dictionary(self):
#         return {
#             'POSTGRES_DB': self.database,
#             'POSTGRES_USER': self.username,
#             'POSTGRES_PASSWORD': self.password
#         }


class EnvironmentVariables:
    values = {}

    def __init__(self, map={}):
        for k, v in map.items():
            self.values[k] = v


class Service:
    name = "sample-service"
    container_name = "sample-service"
    image = ""
    version = ""
    environment_variables: EnvironmentVariables = None

    def __init__(self,
                 image: str,
                 image_version: str,
                 variables={},
                 name: str = "sample-service",
                 container_name: str = "sample-service"
                 ):
        self.image = image
        self.version = image_version
        self.name = name
        self.container_name = container_name
        self.environment_variables = EnvironmentVariables(variables)
        print(self.environment_variables)

    def to_string(self):
        service_format = service_string
        service_format = service_format.replace("**service-name**", self.name)
        service_format = service_format.replace("**image**", self.image)
        service_format = service_format.replace("**version**", self.version)
        service_format = service_format.replace(
            "**container-name**", self.container_name)
        service_format = service_format.replace(
            "**environment**",
            map_dict_to_string(self.environment_variables.values)
        )
        return service_format


class ComposeFile:
    compose_format = compose_string
    version = "3.8"
    services = []

    def __init__(self, version: str = "3.8", services=[]):
        self.version = version
        self.services = services
        if (services != []):
            self.compose_format = compose_full_string
