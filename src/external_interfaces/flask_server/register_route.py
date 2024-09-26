from flask_openapi3 import OpenAPI

from src.external_interfaces.flask_server.routers import home
from src.external_interfaces.flask_server.routers.application_score import (
    application_score
)
from src.external_interfaces.flask_server.routers import handler_error


def register_route(app: OpenAPI) -> None:
    """
    Função responsável por registrar as rotas no flask
    """
    app.register_api(home.blueprint)
    app.register_api(handler_error.blueprint)
    app.register_api(application_score.blueprint)
