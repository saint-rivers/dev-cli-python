import app.constants.database as database
from app.compose import init
from app.compose.models import ComposeFile
from app.mapper import mapper
from app.services.models import FromDockerfile, PortMapping
from app.docker import docker_writer as docker
import typer


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
    docker.write_dockerfile(file_type)


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
