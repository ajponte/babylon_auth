"""
Health route.
"""
from http import HTTPStatus
from fastapi import APIRouter
from fastapi.responses import JSONResponse

HEALTH_URI = '/health/'

router = APIRouter()

@router.get(HEALTH_URI, tags=['health'])
async def health() -> JSONResponse:
    """Health controller."""
    return JSONResponse(content={'status': 'ok'}, status_code=HTTPStatus.OK)
