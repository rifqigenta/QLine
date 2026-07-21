from flask import Flask

from app.exceptions.errors import AppException
from app.utils.response import error


def register_error_handlers(app: Flask):

    @app.errorhandler(AppException)
    def handle_app_exception(exc: AppException):
        return error(
            exc.message,
            exc.status_code,
        )

    @app.errorhandler(404)
    def handle_404(_):
        return error(
            "Endpoint not found",
            404,
        )

    @app.errorhandler(500)
    def handle_500(_):
        return error(
            "Internal server error",
            500,
        )