class AppException(Exception):
    def __init__(
        self,
        message: str,
        status_code: int = 400,
    ):
        super().__init__(message)

        self.message = message
        self.status_code = status_code


class NotFoundException(AppException):
    def __init__(self, message="Resource not found"):
        super().__init__(
            message,
            404,
        )


class BadRequestException(AppException):
    def __init__(self, message="Bad request"):
        super().__init__(
            message,
            400,
        )


class UnauthorizedException(AppException):
    def __init__(self, message="Unauthorized"):
        super().__init__(
            message,
            401,
        )