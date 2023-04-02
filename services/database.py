from services.models import Service
from services import PortMapping


def postgres():
    return Service(
        image="postgres",
        image_version="14.4-alpine",
        variables={'POSTGRES_DB': 'default',
                   'POSTGRES_USER': 'postgres',
                   'POSTGRES_PASSWORD': 'password'
                   },
        container_name="postgres-db",
        name="postgres-db",
        ports=[PortMapping("5432", "5432")]
    )


def mongodb():
    return Service(
        image="mongo",
        image_version="6.0.1-focal",
        variables={'MONGO_INITDB_ROOT_USERNAME': 'admin',
                   'MONGO_INITDB_ROOT_PASSWORD': 'mongo'
                   },
        container_name="mongodb",
        name="mongodb",
        ports=[PortMapping("27017", "27017")]
    )
