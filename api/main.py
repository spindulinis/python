from fastapi import APIRouter

from api.routes import category, attribute, authentication, products, users

api_router = APIRouter()
api_router.include_router(users.router)
api_router.include_router(products.router)
api_router.include_router(category.router)
api_router.include_router(attribute.router)
api_router.include_router(authentication.router)


