import constants.database as database
from compose import init
import typer
from compose.models import ComposeFile
from mapper import mapper

from services.models import FromDockerfile, PortMapping


app = typer.Typer()


@app.command()
def compose(command: str):

    # comp = ComposeFile(services=[
    #     database.mongodb(), database.postgres(),
    # ])
    comp = ComposeFile(services=[
        FromDockerfile(ports=[PortMapping("8800", "8080"),
                       PortMapping("8443", "8443")])
    ])

    switch = {
        'init': init(comp),
    }
    return switch.get(command, "invalid input")


@app.command()
def dockerfile(file_type: str):
    switch = {
    }
    return switch.get(file_type, "specified dockerfile not available")


@app.command()
def service(service_type: str):
    switch = {
        'postgres': database.postgres(),
        'mongodb': database.mongodb()
    }
    service = switch.get(service_type, "service not provided")
    output = mapper.map_service(service)
    print(output)
    return


app()
