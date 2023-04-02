import services.database as database
from compose import init
import typer
from compose.models import ComposeFile
from mapper import mapper


app = typer.Typer()


@app.command()
def compose(command: str):

    comp = ComposeFile(services=[
        database.mongodb(), database.postgres(),
    ])

    switch = {
        'init': init(comp),
    }
    return switch.get(command, "invalid input")


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
