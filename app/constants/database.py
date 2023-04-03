from app.services.models import Service
from app.services import PortMapping


def postgres():
    env = {'POSTGRES_DB': 'default',
           'POSTGRES_USER': 'postgres',
           'POSTGRES_PASSWORD': 'password'
           }
    service = Service(
        image="postgres",
        image_version="14.4-alpine",
        variables=env,
        container_name="postgres-db",
        name="postgres-db",
        ports=[PortMapping("5432", "5432")]
    )
    return service


def mongodb():
    env = {'MONGO_INITDB_ROOT_USERNAME': 'admin',
           'MONGO_INITDB_ROOT_PASSWORD': 'mongo'
           }
    service = Service(
        image="mongo",
        image_version="6.0.1-focal",
        variables=env,
        container_name="mongodb",
        name="mongodb",
        ports=[PortMapping("27017", "27017")]
    )
    return service
