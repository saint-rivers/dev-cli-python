from app.services import Service, FromDockerfile, Formattable, PortMapping
import app.constants.format as format


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


def map_availble_env(input: str, env: dict[str, str]) -> str:
    if env != {}:
        mapped_env = map_env(env)
        input = input.replace("**environment**", mapped_env)
    else:
        input = input.replace(f"\n    environment: **environment**", "")
    return input


def map_available_ports(input: str, ports: list[PortMapping]) -> str:
    if ports != []:
        mapped_ports = map_ports(ports)
        input = input.replace("**ports**", mapped_ports)
    else:
        input = input.replace(f"\n    ports: **ports**", "")
    return input


def map_base_service(output: str, service: Formattable) -> str:
    output = output.replace("**service-name**", service.name)
    output = output.replace("**container-name**", service.container_name)
    output = map_availble_env(output, service.env)
    output = map_available_ports(output, service.ports)
    return output


def map_service(service: Formattable) -> str:
    output = ""
    if type(service) is FromDockerfile:
        output = format.dockerfile_build_string
        output = output.replace("**context**", service.context)
        output = output.replace("**dockerfile**", service.dockerfile)
    elif type(service) is Service:
        output = format.service_string
        output = output.replace("**image**", service.image)
        output = output.replace("**version**", service.version)
    else:
        print("invalid service type found")

    output = map_base_service(output=output, service=service)
    return output
