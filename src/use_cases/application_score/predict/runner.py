from dataclasses import dataclass
from src.interface_adapters.schemas.application_score.application_score import BodyApplicationScore
from .feature_enginering import FeatureEngineering
from .data_scaler_transformer import DataScalerTransformer
from .predict import Predict
from .explaner import Explaner
import pandas as pd


@dataclass
class Runner:
    body: BodyApplicationScore

    def execute(self) -> pd.DataFrame:
        dir_models = 'src/use_cases/application_score/models'
        feature_enginering = FeatureEngineering(self.body)
        data = feature_enginering.create_features()
        # transformer = DataScalerTransformer(f'{dir_models}/scaler.pkl', data)
        # scaled_data = transformer.transform()
        predict = Predict(data, f'{dir_models}/model.pkl')
        classifiy = predict.execute()

        explaner = Explaner(classifiy, f'{dir_models}/explainer.pkl')
        image = explaner.execute()
        classifiy['shap_plot'] = image
        classifiy['prob_perc'] = classifiy['prob'].mul(100).round(2)
        return classifiy[['identifier', 'prob_perc', 'classify', 'shap_plot']]
