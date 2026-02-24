from fastapi import APIRouter

from api.routes import category, products, users

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(products.router)
api_router.include_router(category.router)


