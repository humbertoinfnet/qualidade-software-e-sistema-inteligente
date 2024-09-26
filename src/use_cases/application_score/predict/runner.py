from dataclasses import dataclass
from src.interface_adapters.schemas.application_score.application_score import BodyApplicationScore
from src.use_cases.application_score.predict import FeatureEngineering, DataScalerTransformer, Predict
import pandas as pd


@dataclass
class Runner:
    body: BodyApplicationScore

    def execute(self) -> pd.DataFrame:
        feature_enginering = FeatureEngineering(self.body)
        data = feature_enginering.create_features()
        transformer = DataScalerTransformer('data_scaler_v2.pkl', data)
        scaled_data = transformer.transform()
        predict = Predict(scaled_data)
        classifiy = predict.execute()
        return classifiy[['identifier', 'prob', 'classify']]
