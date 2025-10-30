from fastapi import FastAPI

from auth_server.logger import get_logger
from auth_server.routers import authenticate, health

APP_NAME = 'babylon_server'

_LOGGER = get_logger()

def create_app() -> FastAPI:
    app = FastAPI(title=APP_NAME)

    _LOGGER.debug('Adding routers')
    app.include_router(health.router)
    app.include_router(authenticate.router)

    return app
