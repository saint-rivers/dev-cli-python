from model import Service


def postgres():
    return Service(
        image="postgres",
        image_version="14.4-alpine",
        variables={'POSTGRES_DB': 'default',
                   'MONGO_INITDB_ROOT_PASSWORD': 'postgres', 'POSTGRES_PASSWORD': 'password'},
        container_name="postgres-db",
        name="postgres-db"
    )


def mongodb():
    return Service(
        image="mongo",
        image_version="6.0.1-focal",
        variables={'MONGO_INITDB_ROOT_USERNAME': 'admin',
                   'MONGO_INITDB_ROOT_PASSWORD': 'mongo'
                   },
        container_name="mongodb",
        name="mongodb"
    )
