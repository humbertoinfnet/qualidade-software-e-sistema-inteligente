import pickle
import pandas as pd


class Predict:
    
    def __init__(self, data, filename):
        self.model = self.load_model(filename)
        self.data = data
    
    def load_model(self, filename):
        with open(filename, 'rb') as file:
            loaded_model = pickle.load(file)
        return loaded_model
    
    def execute(self) -> pd.DataFrame:
        prob = self.model.predict_proba(self.data.get(self.model.feature_names_in_))[:, 1]
        classify = self.classify(prob)
        self.data['prob'] = prob
        self.data['classify'] = classify.tolist()
        return self.data
        
    def classify(self, prob):
        bins = [0.05, 0.15, 0.3, 0.4, 0.7, 0.8, 0.9, 0.95]
        labels = ['AA','A', 'B', 'C', 'D', 'E', 'F']
        return pd.cut(prob, bins=bins, labels=labels)
