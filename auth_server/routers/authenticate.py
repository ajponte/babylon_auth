"""Auth controller."""
from http import HTTPStatus
from fastapi import APIRouter

AUTHENTICATE_URI = '/authenticate/'

router = APIRouter()

@router.post(AUTHENTICATE_URI, tags=['authenticate'])
async def authenticate() -> tuple[dict, int]:
    return {}, HTTPStatus.OK
