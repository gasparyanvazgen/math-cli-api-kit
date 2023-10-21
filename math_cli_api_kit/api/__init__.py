"""This module defines and configures the Sanic application for the
Math API.

It sets up the Sanic app with the specified configurations, including
API metadata and settings, and registers the OpenAPI3 Blueprint and the
math operations Blueprint.
"""

from sanic import Sanic
from sanic_openapi import openapi3_blueprint

from .main.blueprint import math_blueprint
from ..config import APIConfig


def create_app(app_name: str) -> Sanic:
    app = Sanic(app_name)
    api_config = APIConfig()

    # set configuration attributes from the Config class
    app.config.API_BASEPATH = api_config.API_BASEPATH
    app.config.API_SCHEMES = api_config.API_SCHEMES
    app.config.API_VERSION = api_config.API_VERSION
    app.config.API_TITLE = api_config.API_TITLE
    app.config.API_DESCRIPTION = api_config.API_DESCRIPTION
    app.config.API_CONTACT_NAME = api_config.API_CONTACT_NAME
    app.config.API_CONTACT_URL = api_config.API_CONTACT_URL
    app.config.API_CONTACT_EMAIL = api_config.API_CONTACT_EMAIL
    app.config.API_LICENSE_NAME = api_config.API_LICENSE_NAME
    app.config.API_LICENSE_URL = api_config.API_LICENSE_URL

    app.blueprint(openapi3_blueprint)
    app.blueprint(math_blueprint)

    return app
