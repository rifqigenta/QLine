from flask import Blueprint, request

from app.services.auth_service import AuthService
from app.utils.response import error, success

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/auth",
)


@auth_bp.post("/login")
def login():
    body = request.get_json(silent=True)

    if body is None:
        return error(
            "Request body is required.",
            400,
        )

    username = body.get("username")
    password = body.get("password")

    if not username or not password:
        return error(
            "Username and password are required.",
            400,
        )

    result = AuthService.login(
        username=username,
        password=password,
    )

    if result is None:
        return error(
            "Invalid username or password.",
            401,
        )

    return success(
        result,
        "Login successful.",
    )