from file import write_to_compose_file
from compose import ComposeFile
from services import Service
from mapper import mapper


def combine_services(services: list[Service]):
    if (len(services) <= 0):
        return ""
    services_as_string = ""
    for s in services:
        service_string = mapper.map_service(s)
        services_as_string = f"{services_as_string}{service_string}"
    return services_as_string


def init(compose: ComposeFile):
    new_file = compose.compose_format
    new_file = new_file.replace("**version**", compose.version)

    services_as_string = combine_services(compose.services)
    new_file = new_file.replace("**services**", services_as_string)

    write_to_compose_file(new_file)

    print("CREATED docker-compose.yml in the current directory")
    print("DONE")
