from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.currency.router import api_currency_router
from api.payment.router import api_payment_router

from config import settings

origins = [
    settings.web_url
]


def create_fastapi_app():
    fastapi_app = FastAPI()
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    fastapi_app.include_router(api_currency_router, prefix="/api/currency")
    fastapi_app.include_router(api_payment_router, prefix="/api/payment")

    return fastapi_app
