service_string = '''
  **service-name**:
    image: **image**:**version**
    container_name: **container-name**
    environment: **environment**
'''

dockerfile_build_string = '''
  **service-name**:
    build:
      context: **context**
      dockerfile: **dockerfile**
    container_name: **container-name**
    environment: **environment**
'''

compose_string = '''version: **version**

'''

compose_full_string = '''version: "**version**"

services: **services**
'''