from typing import Optional, Literal
from pydantic import BaseModel, Field, RootModel
import uuid


class ResponseApplicationScore(BaseModel):
    identifier: str = Field('uuid', description="ID do cliente")
    classify: str = Field('D', description='Classificação de risco')
    prob: float = Field(0.00, description='Rating')
    shap_plot: str = Field('codigo imagem base64', description='Imagem da explicação da classificação do modelo')

class ResponseSuccessApplicationScore(RootModel):
    root: list[ResponseApplicationScore] = Field(description="Array dos objetos")


class BodyApplicationScore(BaseModel):
    identifier: str = Field(default_factory=lambda: str(uuid.uuid4()), description="ID do cliente")
    limite_credito: float = Field(..., description="Limite de crédito")
    sexo: int = Field(1, description="Sexo do cliente (1 = Masculino, 2 = Feminino)", ge=1, le=2)
    escolaridade: int = Field(3, description="Nível de escolaridade (0 a 6)", ge=0, le=6)
    estado_civil: int = Field(1, description="Estado civil (1 = Casado, 2 = Solteiro, 3 = Outros)", ge=0, le=3)
    idade: int = Field(..., description="Idade do cliente")
    status_pag_1: int = Field(..., description="Status de pagamento no mês mais recente", ge=-2, le=7)
    status_pag_2: int = Field(..., description="Status de pagamento no segundo mês mais recente", ge=-2, le=7)
    status_pag_3: int = Field(..., description="Status de pagamento no terceiro mês mais recente", ge=-2, le=7)
    status_pag_4: int = Field(..., description="Status de pagamento no quarto mês mais recente", ge=-2, le=7)
    status_pag_5: int = Field(..., description="Status de pagamento no quinto mês mais recente", ge=-2, le=7)
    status_pag_6: int = Field(..., description="Status de pagamento no sexto mês mais recente", ge=-2, le=7)
    fatura_1: float = Field(..., description="Valor da fatura no mês mais recente")
    fatura_2: float = Field(..., description="Valor da fatura no segundo mês mais recente")
    fatura_3: float = Field(..., description="Valor da fatura no terceiro mês mais recente")
    fatura_4: float = Field(..., description="Valor da fatura no quarto mês mais recente")
    fatura_5: float = Field(..., description="Valor da fatura no quinto mês mais recente")
    fatura_6: float = Field(..., description="Valor da fatura no sexto mês mais recente")
    pag_fatura_1: float = Field(..., description="Valor pago no mês mais recente")
    pag_fatura_2: float = Field(..., description="Valor pago no segundo mês mais recente")
    pag_fatura_3: float = Field(..., description="Valor pago no terceiro mês mais recente")
    pag_fatura_4: float = Field(..., description="Valor pago no quarto mês mais recente")
    pag_fatura_5: float = Field(..., description="Valor pago no quinto mês mais recente")
    pag_fatura_6: float = Field(..., description="Valor pago no sexto mês mais recente")