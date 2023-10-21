"""This module defines the API blueprint for the math
operations' calculator. It contains routes for algebraic and geometric
operations, which are implemented in the AlgebraAPI and GeometryAPI
classes.

The routes include endpoints for performing algebraic and geometric
calculations and are prefixed with '/{APIConfig.API_BASEPATH}/math/api'.
"""

from sanic import Blueprint

from .math_api import AlgebraAPI, GeometryAPI
from ....config import APIConfig

math_blueprint = Blueprint(
    name="Math-API",
    url_prefix=f"/{APIConfig.API_BASEPATH}/math/api"
)

math_blueprint.add_route(
    handler=AlgebraAPI.as_view(),
    uri="/algebra/<operation>",
    strict_slashes=True,
    name="algebra_operation",
)

math_blueprint.add_route(
    handler=GeometryAPI.as_view(),
    uri="/geometry/<operation>",
    strict_slashes=True,
    name="geometry_operation",
)
