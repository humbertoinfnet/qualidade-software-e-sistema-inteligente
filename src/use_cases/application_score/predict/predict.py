import pickle
import pandas as pd


class Predict:
    
    def __init__(self, data):
        self.model = self.load_model()
        self.data = data
    
    def load_model(self):
        with open('random_forest_model_v2.pkl', 'rb') as file:
            loaded_model = pickle.load(file)
        return loaded_model
    
    def execute(self) -> pd.DataFrame:
        prob = self.model.predict_proba(self.data.get(self.model.feature_names_in_))[:, 1]
        classify = self.classify(prob)
        self.data['prob'] = prob
        self.data['classify'] = classify.tolist()
        return self.data
        
    def classify(self, prob):
        bins = [0, 0.1, 0.2, 0.3, 0.8, 0.85, 0.93, 0.95]  # Intervalos ajustados
        labels = ['AA','A', 'B', 'C', 'D', 'E', 'F']
        return pd.cut(prob, bins=bins, labels=labels)