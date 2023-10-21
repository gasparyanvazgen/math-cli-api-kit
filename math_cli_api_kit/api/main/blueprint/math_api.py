"""This module defines the API endpoints for performing math
operations using the AlgebraAPI and GeometryAPI classes. It provides
APIs for algebraic and geometric operations such as addition,
subtraction, multiplication, division, powers, square root, factorial,
and exponential functions.

The AlgebraAPI class handles algebraic operations, and the GeometryAPI
class handles geometric operations. These operations can be performed
by making POST requests to the respective endpoints.

The API endpoints support JSON input data for performing the
operations, and they return JSON responses with the results and status
messages. The module also includes OpenAPI documentation for each
endpoint, specifying the input format, response format, and error handling.
"""

from sanic import Request, HTTPResponse, json
from sanic.exceptions import SanicException
from sanic.views import HTTPMethodView
from sanic_openapi.openapi3 import openapi

from math_cli_api_kit.config import APIConfig
from math_cli_api_kit.core.math_operations import Algebra, Geometry

_algebra = Algebra()
_geometry = Geometry()


class AlgebraOperands:
    x: float
    y: float


class GeometryOperands:
    a: float
    b: float
    h: float
    r: float


class AlgebraAPI(HTTPMethodView):
    """This class defines an API for algebraic operations."""

    @openapi.description("API for performing algebraic operations, including"
                         " addition, subtraction, multiplication, division,"
                         " and powers.")
    @openapi.summary("Performs algebraic operations based on the provided"
                     " 'operation' parameter. The 'operation' parameter must"
                     " be one of the supported operations: 'sum', 'sub', "
                     "'mul', 'div', 'pow'.")
    @openapi.body(
        {"application/json": AlgebraOperands},
        description="Input data for algebraic operations. The format depends"
                    " on the 'operation' specified.",
        required=True
    )
    @openapi.response(
        200, {"result": float, "message": str},
        description="Success - The operation was successful."
    )
    @openapi.response(
        400, {"message": str},
        description="Bad request - Invalid input data."
    )
    @openapi.response(
        500, {"message": str},
        description="Internal server error - Something went wrong during"
                    " the operation."
    )
    async def post(self, request: Request, operation: str) -> HTTPResponse:
        if operation in ("sum", "sub", "mul", "div", "pow"):
            x, y = request.json["x"], request.json["y"]

            if operation == "sum":
                return json(
                    {"results": _algebra.sum(x, y), "message": "Success"},
                    status=200
                )
            elif operation == "sub":
                return json(
                    {"results": _algebra.sub(x, y), "message": "Success"},
                    status=200
                )
            elif operation == "mul":
                return json(
                    {"results": _algebra.mul(x, y), "message": "Success"},
                    status=200
                )
            elif operation == "div":
                return json(
                    {"results": _algebra.div(x, y), "message": "Success"},
                    status=200
                )
            else:
                return json(
                    {"results": _algebra.pow(x, y), "message": "Success"},
                    status=200
                )
        elif operation in ("square_root", "factorial", "exp"):
            x = request.json["x"]

            if operation == "square_root":
                return json(
                    {"results": _algebra.square_root(x), "message": "Success"},
                    status=200
                )
            elif operation == "factorial":
                return json(
                    {"results": _algebra.factorial(x), "message": "Success"},
                    status=200
                )
            else:
                return json(
                    {"results": _algebra.exp(x), "message": "Success"},
                    status=200
                )
        else:
            raise SanicException(
                message=f"Requested URL {APIConfig.API_BASEPATH}/math/api"
                        f"/algebra/{operation} not found",
                status_code=404
            )


class GeometryAPI(HTTPMethodView):
    """This class defines an API for geometric operations."""

    @openapi.description("API for performing geometric operations, including"
                         " surface of a square, circle, triangle, trapezoid,"
                         " and hypotenuse.")
    @openapi.summary("Performs geometric operations based on the provided"
                     " 'operation' parameter. The 'operation' parameter must"
                     " be one of the supported operations:"
                     " 'surface_of_square', 'surface_of_circle',"
                     " 'surface_of_triangle', 'surface_of_trapezoid',"
                     " 'hypotenuse'.")
    @openapi.body(
        {"application/json": GeometryOperands},
        description="Input data for geometric operations. The format depends"
                    " on the 'operation' specified.",
        required=True
    )
    @openapi.response(
        200, {"result": float, "message": str},
        description="Success - The operation was successful."
    )
    @openapi.response(
        400, {"message": str},
        description="Bad request - Invalid input data."
    )
    @openapi.response(
        500, {"message": str},
        description="Internal server error - Something went wrong during"
                    " the operation."
    )
    async def post(self, request: Request, operation: str) -> HTTPResponse:
        if operation in ("surface_of_square", "surface_of_trapezoid",
                         "hypotenuse"):
            a = request.json["a"]

            if operation == "surface_of_square":
                return json(
                    {
                        "result": _geometry.surface_of_square(a),
                        "message": "Success"
                    }, status=200
                )
            else:
                b = request.json.get("b")

                if operation == "surface_of_trapezoid":
                    h = request.json.get("h")
                    return json(
                        {
                            "result": _geometry.surface_of_trapezoid(a, b, h),
                            "message": "Success"
                        }, status=200
                    )
                else:
                    return json(
                        {
                            "result": _geometry.hypotenuse(a, b),
                            "message": "Success"
                        }, status=200
                    )
        elif operation == "surface_of_circle":
            r = request.json.get("r")
            return json(
                {
                    "result": _geometry.surface_of_circle(r),
                    "message": "Success"
                }, status=200
            )
        elif operation == "surface_of_triangle":
            b, h = request.json.get("b"), request.json.get("h")
            return json(
                {
                    "result": _geometry.surface_of_triangle(b, h),
                    "message": "Success"
                }, status=200
            )
        else:
            raise SanicException(
                message=f"Requested URL {APIConfig.API_BASEPATH}/math/api"
                        f"/geometry/{operation} not found",
                status_code=404
            )
