from fastapi import APIRouter

from api.routes import category, attribute, authentication, product, public_product, user

api_router = APIRouter()
api_router.include_router(user.router)
api_router.include_router(product.router)
api_router.include_router(public_product.router)
api_router.include_router(category.router)
api_router.include_router(attribute.router)
api_router.include_router(authentication.router)


