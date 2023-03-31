
def write_to_compose_file(content: str):
    with open('docker-compose.yml', 'w') as compose:
        compose.write(content)
