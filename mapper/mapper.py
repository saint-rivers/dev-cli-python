# from services.models import PortMapping
from services import Service, Dockerfile, Formattable, PortMapping
import format


def map_env(map: dict[str, str]):
    envs = ""
    for k, v in map.items():
        envs = f"{envs}\n      - {k}={v}"
    return envs


def map_ports(ports=list[PortMapping]):
    output = ""
    for m in ports:
        output = f"{output}\n      - \"{m.host_port}:{m.container_port}\""
    return output


def map_base_service(output: str, service: Formattable) -> str:
    output = output.replace("**service-name**", service.name)
    output = output.replace("**container-name**", service.container_name)

    if service.env.values != None:
        mapped_env = map_env(service.env.values)
        output = output.replace("**environment**", mapped_env)

    if service.ports != None:
        mapped_ports = map_ports(service.ports)
        output = output.replace("**ports**", mapped_ports)

    return output


def map_service(service: Formattable) -> str:
    output = ""
    if type(service) is Dockerfile:
        output = format.dockerfile_build_string
        output = output.replace("**context**", service.context)
        output = output.replace("**dockerfile**", service.dockerfile)
    elif type(service) is Service:
        output = format.service_string
        output = output.replace("**image**", service.image)
        output = output.replace("**version**", service.version)
    else:
        print("invalid service type found")

    output = map_base_service(output, service)
    return output
