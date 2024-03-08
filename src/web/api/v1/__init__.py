# src/web/api/v1/__init__.py
from flask import Blueprint
from flask_restx import Api
from .time_service import TimeService

blueprint = Blueprint("api_v1", __name__)
api_v1 = Api(
    blueprint,
    version="1.0",
    title="API Gateway - Version 1",
    description="API Gateway with Swagger support - Version 1",
)

namespace_v1 = api_v1.namespace("v1", description="API version 1")
namespace_v1.add_resource(TimeService, "/time")
