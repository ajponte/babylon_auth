"""
Health route.
"""
from pydantic import BaseModel
from http import HTTPStatus
from fastapi import APIRouter
from fastapi.responses import JSONResponse

HEALTH_URI = '/health/'

router = APIRouter()

class HealthResponse(BaseModel):
    status: str

@router.get(HEALTH_URI, tags=['health'])
async def health() -> JSONResponse:
    return JSONResponse(content={'status': 'ok'}, status_code=HTTPStatus.OK)
