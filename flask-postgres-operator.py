import kopf
import asyncio
from kubernetes import client
from helm_python.Helm import Helm
import os
import yaml

POSTGRES_POD = "postgresdb-postgresql-0"
NAMESPACE = "kopf-helm-2-tier"


# We first install postgres on start of the operator
# Helm will upgrade if its already installed
@kopf.on.startup()
async def startup_fn(logger, **kwargs):
    logger.info("Starting operator")
    global LOCK
    LOCK = asyncio.Lock()  # uses the running asyncio loop by default
    helm = Helm()
    helm.upgrade(
        name = "postgresdb",
        path = "oci://registry-1.docker.io/bitnamicharts/postgresql",
        namespace = NAMESPACE,
        sets= [
            {'name': "auth.username", 'value': 'postgres'},
            {'name': "auth.password", 'value': "postgres"},
        ]
    )
    logger.info("Complete Start")

    
# This is triggered from the "Postgres" installation 
# But there are better ways to do this but shows
# that conceptually you can listen to events of the Helm deployment
@kopf.on.create('Pod')
async def create_fn(spec, name, namespace, logger, **kwargs):
    
    # When we're done 
    # We could probably also check the health of the pod
    if name == POSTGRES_POD and namespace == "kopf-helm-2-tier":

        logger.info(f"###### Pod creation event from {namespace}/{name} ")
        path = os.path.join(os.path.dirname(__file__), 'flask/deployment.yaml')
        tmpl = open(path, 'rt').read()
        data = yaml.safe_load(tmpl)

        api = client.AppsV1Api()
        
        obj = api.create_namespaced_deployment(
            namespace=namespace,
            body=data,
        )

