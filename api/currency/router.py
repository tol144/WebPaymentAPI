from fastapi import APIRouter

from api.currency.enum import CurrencyEnum


api_currency_router = APIRouter()


@api_currency_router.get("/",
                 response_model=list[str],
                 summary="Список валют")
async def currency_list() -> list[str]:
    return list(CurrencyEnum)
