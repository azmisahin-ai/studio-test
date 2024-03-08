# src/web/api/__init__.py
from flask import Blueprint
from flask_restx import Api
from .v1 import namespace_v1
from .v2 import namespace_v2

blueprint = Blueprint("api", __name__)
api = Api(
    blueprint,
    version="0.0.1",
    title="API Gateway",
    description="API Gateway with Swagger support",
)

# Add the namespaces and resources directly to the main API
api.add_namespace(namespace_v1, path="/v1")
api.add_namespace(namespace_v2, path="/v2")
