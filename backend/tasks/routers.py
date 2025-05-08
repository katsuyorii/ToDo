from fastapi import APIRouter


tasks_router = APIRouter(
    prefix='/tasks',
    tags=['Tasks'],
)

