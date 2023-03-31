# import typer
from compose import init
import typer
from model import ComposeFile, Service

app = typer.Typer()


@app.command()
def compose(command: str):
    service = Service(
        variables={'POSTGRES_DB': 'default',
                   'POSTGRES_USER': 'postgres',
                   'POSTGRES_PASSWORD': 'password'
                   },
        container_name="myservice",
        image="postgres",
        image_version="14.4-alpine"
    )
    switch = {
        'init': init(ComposeFile(services=[service])),
    }
    return switch.get(command, "invalid input")


@app.command()
def service(service_type: str):
    switch = {
        'postgres': Service(
            variables={'POSTGRES_DB': 'default',
                       'POSTGRES_USER': 'postgres', 'POSTGRES_PASSWORD': 'password'},
            container_name="myservice",
            image="postgres",
            image_version="14.4-alpine"
        )
    }
    return switch.get(service_type, "service not provided")


app()
