from dataclasses import dataclass
import pandas as pd
import numpy as np
from src.interface_adapters.schemas.application_score.application_score import BodyApplicationScore


@dataclass
class FeatureEngineering:
    data: BodyApplicationScore

    def create_features(self) -> pd.DataFrame:
        # Features baseadas no comportamento de pagamento
        self.data = pd.DataFrame(self.data)
        self.data['avg_payment'] = self.data[['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']].mean(axis=1)
        self.data['min_pay_prop'] = self.data['PAY_AMT1'] / self.data['BILL_AMT1']
        self.data['consecutive_late_payments'] = self.data[['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']].apply(lambda x: (x <= 0).sum(), axis=1)

        # Features baseadas na utilização do crédito
        self.data['debt_ratio'] = self.data['BILL_AMT1'] / self.data['LIMIT_BAL']
        self.data['credit_utilization'] = self.data['BILL_AMT1'] / self.data['LIMIT_BAL']
        self.data['monthly_spending_variation'] = self.data['BILL_AMT1'].pct_change()

        # Features baseadas no perfil do cliente
        self.data['age_group'] = pd.cut(self.data['AGE'], bins=[20, 30, 40, 50, 60, 70], labels=['20s', '30s', '40s', '50s', '60+'])
        self.data['sex_education'] = self.data['SEX'].astype(str) + '_' + self.data['EDUCATION'].astype(str)

        # Novas features
        self.data['total_paid_amount'] = self.data[['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']].sum(axis=1)
        self.data['full_payment_prop'] = (self.data['PAY_AMT1'] == self.data['BILL_AMT1']).mean() * 100
        self.data['months_since_last_full_payment'] = self.data.apply(lambda row: next((i for i, x in enumerate(row[['PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6']]) if x == row['BILL_AMT1']), 6), axis=1)

        self.data['marriage_age_group'] = self.data['MARRIAGE'].astype(str) + '_' + self.data['age_group'].astype(str)

        # Features anteriores (já mencionadas)
        self.data['max_bill_amount'] = self.data[['BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']].max(axis=1)
        self.data['min_bill_amount'] = self.data[['BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']].min(axis=1)
        self.data['payment_frequency'] = self.data[['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']].apply(lambda x: (x > 0).sum(), axis=1)
        self.data['recent_payment_trend'] = self.data['PAY_AMT1'] - self.data['PAY_AMT6']
        self.data['has_ever_defaulted'] = (self.data[['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']] <= 0).any(axis=1).astype(int)
        
        # Exemplo: Razão de utilização de crédito
        self.data['credit_utilization_ratio'] = self.data['BILL_AMT1'] / self.data['LIMIT_BAL']
        
        # Exemplo: Razão entre o pagamento mínimo e o pagamento total
        self.data['min_pay_ratio'] = self.data['PAY_AMT1'] / self.data['BILL_AMT1']
        
        # Exemplo: Diferença entre fatura e pagamento
        self.data['diff_bill_payment_1'] = self.data['BILL_AMT1'] - self.data['PAY_AMT1']
        
        # Exemplo: Número de atrasos nos últimos meses
        self.data['num_late_payments'] = (self.data[['PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6']] > 0).sum(axis=1)
        
        # Exemplo: Atrasos consecutivos
        self.data['consecutive_late_payments'] = self.data[['PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6']].apply(lambda row: row.gt(0).cumsum().max(), axis=1)
        
        # Exemplo: Variação nos gastos mensais
        self.data['monthly_spending_variation'] = self.data['BILL_AMT1'] - self.data['BILL_AMT2']
        
        # Exemplo: Tempo desde o último pagamento completo
        self.data['months_since_last_full_payment'] = (self.data[['PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']].values < self.data[['BILL_AMT1', 'BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6']].values).sum(axis=1)        
        
        self.data.replace([np.inf, -np.inf], np.nan, inplace=True)
        return self.data