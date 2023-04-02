import services.database as database
from compose import init
import typer
from compose.models import ComposeFile


app = typer.Typer()


@app.command()
def compose(command: str):
    service = database.postgres()
    switch = {
        'init': init(ComposeFile(services=[
            database.mongodb(), database.postgres(),
        ])),
    }
    return switch.get(command, "invalid input")


@app.command()
def service(service_type: str):
    switch = {
        'postgres': database.postgres(),
        'mongodb': database.mongodb()
    }
    return switch.get(service_type, "service not provided")


app()
