from dataclasses import dataclass
import pandas as pd
import numpy as np
from src.interface_adapters.schemas.application_score.application_score import BodyApplicationScore


@dataclass
class FeatureEngineering:
    data: BodyApplicationScore

    def create_features(self) -> pd.DataFrame:
        # Features baseadas no comportamento de pagamento
        self.data = pd.DataFrame([self.data.model_dump()])

        self.data['num_pag_nao_pagos_total'] = self.data[['pag_fatura_1', 'pag_fatura_2', 'pag_fatura_3', 'pag_fatura_4', 'pag_fatura_5', 'pag_fatura_6']].apply(lambda x: (x <= 0).sum(), axis=1)
        # Taxa de Utilização de Crédito
        self.data['utilizacao_credito'] = (self.data['fatura_1'] + self.data['fatura_2'] + self.data['fatura_3'] + 
                                self.data['fatura_4'] + self.data['fatura_5'] + self.data['fatura_6']) / self.data['limite_credito']

        # Diferença entre Pagamento e Fatura
        for i in range(1, 7):
            self.data[f'dif_pag_fatura_{i}'] = self.data[f'pag_fatura_{i}'] - self.data[f'fatura_{i}']

        # Média de Pagamentos
        self.data['media_pagamentos'] = (self.data['pag_fatura_1'] + self.data['pag_fatura_2'] + self.data['pag_fatura_3'] + 
                                self.data['pag_fatura_4'] + self.data['pag_fatura_5'] + self.data['pag_fatura_6']) / 6

        # Número de Atrasos
        self.data['numero_atrasos'] = (self.data[['status_pag_1', 'status_pag_2', 'status_pag_3', 'status_pag_4', 'status_pag_5', 'status_pag_6']] > 0).sum(axis=1)
        self.data.replace([np.inf, -np.inf], 0, inplace=True)
        return self.data