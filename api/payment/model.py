from pydantic import BaseModel


class CreatePaymentModel(BaseModel):
    user_id: int
    currency: str
    amount: int


class PaymentTariffModel(BaseModel):
    name: str
    amount: int
