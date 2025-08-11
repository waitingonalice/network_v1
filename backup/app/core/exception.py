from typing import List, Optional
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class BaseServiceExceptionHandler(Exception):
    def __init__(
        self,
        service_code: str,
        status_code: int = 500,
        message: str = "Internal server error",
        custom_status_code: Optional[str] = None,
    ):
        self.message = message
        self.service_code = service_code
        self.status_code = status_code
        self.custom_status_code = custom_status_code


class ErrorResponse(BaseModel):
    error_code: str
    message: str

    @staticmethod
    def from_exception(status_code: int, error_code: str, message: str):
        return JSONResponse(
            status_code=status_code,
            content=ErrorResponse(
                error_code=error_code,
                message=message,
            ).model_dump(),
        )


class RouteExceptionHandler:

    @staticmethod
    def __create_exception_handler():
        def handler(request: Request, exc: BaseServiceExceptionHandler):
            code = exc.custom_status_code or exc.status_code
            error_code = f"{exc.service_code}{code}"
            return ErrorResponse.from_exception(
                status_code=exc.status_code,
                error_code=error_code,
                message=exc.message,
            )

        return handler

    @staticmethod
    def add_exception(
        app: FastAPI,
        service_exception_handlers: List[type[BaseServiceExceptionHandler]],
    ):
        for handler in service_exception_handlers:
            app.add_exception_handler(
                exc_class_or_status_code=handler,
                handler=RouteExceptionHandler.__create_exception_handler(),
            )
