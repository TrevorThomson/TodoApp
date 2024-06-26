
from fastapi import APIRouter
from .todo import router as todo

router = APIRouter(prefix='/v1')

router.include_router(todo.router, prefix='/todo', tags=['todo'])
