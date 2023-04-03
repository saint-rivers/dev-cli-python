service_string = '''
  **service-name**:
    image: **image**:**version**
    container_name: **container-name**
    environment: **environment**
    ports: **ports**
'''

dockerfile_build_string = '''
  **service-name**:
    build:
      context: **context**
      dockerfile: **dockerfile**
    container_name: **container-name**
    environment: **environment**
    ports: **ports**
'''

compose_string = '''version: **version**

'''

compose_full_string = '''version: "**version**"

services: **services**
'''

jre_string = '''FROM eclipse-temurin:17-jre-alpine
ADD build/libs/*.jar /opt/root.jar
ENTRYPOINT ["java","-jar","/opt/root.jar"]
'''

keycloak_string = '''FROM quay.io/keycloak/keycloak:21.0 as builder
ENV KC_HEALTH_ENABLED=true
ENV KC_METRICS_ENABLED=true

# Configure a database vendor
ENV KC_DB=postgres

WORKDIR /opt/keycloak
RUN /opt/keycloak/bin/kc.sh build

# run the optimized build
FROM quay.io/keycloak/keycloak:21.0.2
COPY --from=builder /opt/keycloak/ /opt/keycloak/
ENTRYPOINT ["/opt/keycloak/bin/kc.sh"]
'''