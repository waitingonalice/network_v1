from fastapi import FastAPI
from app.core.exception import RouteExceptionHandler
from app.routes.backup import backup_router_v1
from app.exceptions.backup import backup_exceptions


def lifespan(app: FastAPI):
    yield


app = FastAPI(
    title="Backup Service",
    lifespan=lifespan,
)


app.include_router(backup_router_v1, prefix="/api")
RouteExceptionHandler.add_exception(
    app=app,
    service_exception_handlers=backup_exceptions,
)


@app.get("/")
def read_root():
    return {"message": "App is running on port 8000"}
