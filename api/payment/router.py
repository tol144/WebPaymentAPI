from fastapi import APIRouter

from api.payment.model import CreatePaymentModel, PaymentTariffModel

api_payment_router = APIRouter()


@api_payment_router.post("/tariff",
                         response_model=list[PaymentTariffModel],
                         summary="Суммы платежей для кнопок")
async def create_payment(user_id: int) -> list[PaymentTariffModel]:
    result = [PaymentTariffModel(name="Один месяц", amount=100),
              PaymentTariffModel(name="Три месяца", amount=300),
              PaymentTariffModel(name="Полгода", amount=500),
              PaymentTariffModel(name="Год", amount=1000)]
    return result


@api_payment_router.post("/create",
                         response_model=str,
                         summary="Создание нового платежа")
async def create_payment(data: CreatePaymentModel) -> str:
    try:
        return "https://t.me/opengater_vpn_bot"
    except ValueError as e:
        return f"detail{str(e)}"
