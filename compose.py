from file import write_to_compose_file
from model import ComposeFile


def combine_services(services):
    if (len(services) <= 0):
        return ""
    services_as_string = ""
    for s in services:
        services_as_string = f"{services_as_string}{s.to_string()}\n\n"
    return services_as_string


def init(compose: ComposeFile):
    new_file = compose.compose_format
    new_file = new_file.replace("**version**", compose.version)

    services_as_string = combine_services(compose.services)
    new_file = new_file.replace("**services**", services_as_string)
    write_to_compose_file(new_file)

    print("CREATED docker-compose.yml in the current directory")
    print("DONE")
