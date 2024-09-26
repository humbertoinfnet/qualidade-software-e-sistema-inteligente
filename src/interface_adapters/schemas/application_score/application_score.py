from typing import Optional
from pydantic import BaseModel, Field, RootModel


class ResponseApplicationScore(BaseModel):
    policy_id: int = Field(None, description='Id da política')
    name: str = Field(None, description='Nome da política')
    description: str = Field(None, description='Descrição da política')
    identify: str = Field(None, description='Identificacao do elemento')


class ResponseSuccessApplicationScore(RootModel):
    root: list[ResponseApplicationScore] = Field(description="Array dos objetos")


class BodyApplicationScore(BaseModel):
    id: int = Field(..., description="Identificador da classidficação do cliente")
    limit_bal: float = Field(..., description="Limite de crédito do cliente")
    sex: int = Field(..., description="Sexo do cliente (1 = Masculino, 2 = Feminino)")
    education: int = Field(..., description="Nível de educação do cliente (1 a 4)")
    marriage: int = Field(..., description="Estado civil (1 = Casado, 2 = Solteiro, 3 = Outros)")
    age: int = Field(..., description="Idade do cliente")
    pay_1: int = Field(..., description="Status de pagamento no mês mais recente")
    pay_2: int = Field(..., description="Status de pagamento no segundo mês mais recente")
    pay_3: int = Field(..., description="Status de pagamento no terceiro mês mais recente")
    pay_4: int = Field(..., description="Status de pagamento no quarto mês mais recente")
    pay_5: int = Field(..., description="Status de pagamento no quinto mês mais recente")
    pay_6: int = Field(..., description="Status de pagamento no sexto mês mais recente")
    bill_amt1: float = Field(..., description="Valor da fatura no mês mais recente")
    bill_amt2: float = Field(..., description="Valor da fatura no segundo mês mais recente")
    bill_amt3: float = Field(..., description="Valor da fatura no terceiro mês mais recente")
    bill_amt4: float = Field(..., description="Valor da fatura no quarto mês mais recente")
    bill_amt5: float = Field(..., description="Valor da fatura no quinto mês mais recente")
    bill_amt6: float = Field(..., description="Valor da fatura no sexto mês mais recente")
    pay_amt1: float = Field(..., description="Valor pago no mês mais recente")
    pay_amt2: float = Field(..., description="Valor pago no segundo mês mais recente")
    pay_amt3: float = Field(..., description="Valor pago no terceiro mês mais recente")
    pay_amt4: float = Field(..., description="Valor pago no quarto mês mais recente")
    pay_amt5: float = Field(..., description="Valor pago no quinto mês mais recente")
    pay_amt6: float = Field(..., description="Valor pago no sexto mês mais recente")

    class Config:
        schema_extra = {
            "example": {
                "id": 123456,
                "limit_bal": 200000.0,
                "sex": 1,
                "education": 2,
                "marriage": 1,
                "age": 35,
                "pay_1": 0,
                "pay_2": -1,
                "pay_3": 0,
                "pay_4": 0,
                "pay_5": -1,
                "pay_6": -1,
                "bill_amt1": 50000.0,
                "bill_amt2": 48000.0,
                "bill_amt3": 47000.0,
                "bill_amt4": 46000.0,
                "bill_amt5": 45000.0,
                "bill_amt6": 44000.0,
                "pay_amt1": 2000.0,
                "pay_amt2": 1500.0,
                "pay_amt3": 1800.0,
                "pay_amt4": 1900.0,
                "pay_amt5": 1600.0,
                "pay_amt6": 1700.0
            }
        }