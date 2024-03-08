# src/web/api/v2/__init__.py
from flask import Blueprint
from flask_restx import Api
from .time_service_v2 import TimeServiceV2  # Assuming you have a separate file for v2

blueprint = Blueprint("api_v2", __name__)
api_v2 = Api(
    blueprint,
    version="2.0",
    title="API Gateway - Version 2",
    description="API Gateway with Swagger support - Version 2",
)

namespace_v2 = api_v2.namespace("v2", description="API version 2")
namespace_v2.add_resource(TimeServiceV2, "/time")
