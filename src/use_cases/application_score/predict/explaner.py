import pickle
import pandas as pd
import io
import matplotlib.pyplot as plt
import base64
import shap


class Explaner:
    
    def __init__(self, data, filename):
        self.explainer = self.load_model(filename)
        self.data = data
    
    def load_model(self, filename):
        with open(filename, 'rb') as file:
            loaded_model = pickle.load(file)
        return loaded_model
    
    def execute(self) -> pd.DataFrame:
        features = self.explainer.feature_names
        shap_values = self.explainer(self.data[features])
        buf = io.BytesIO()
        plt.figure(figsize=(10, 8))
        plot = shap.waterfall_plot(shap_values[0][:,1], max_display=25, show=False,)
        # fig = plt.gcf()
        # fig.set_size_inches(12, 8)
        # fig.savefig(buf, format='png')
        plt.gcf().set_size_inches(12, 7)
        plt.tight_layout()
        plt.savefig(buf, format='png')
        byte_data = buf.getvalue()
        base64_string = base64.b64encode(byte_data).decode('utf-8')
        return base64_string
