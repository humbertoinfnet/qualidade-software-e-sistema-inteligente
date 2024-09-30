from concurrent.futures import ThreadPoolExecutor
import pickle


class DataScalerTransformer:
    def __init__(self, scaler_filename, data):
        self.data = data
        self.scaler = self.load(scaler_filename)

    def load(self, filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
        
    def input_na_numeric(self, columns):
        self.data[columns] = self.scaler.get('imputer_mean').transform(self.data[columns])

    def input_na_categorical(self, columns):
        self.data[columns] = self.scaler.get('imputer_mode').transform(self.data[columns])

    def scale_monetary_columns(self, columns):
        self.data[columns] = self.scaler.get('robust_scaler').transform(self.data[columns])

    def scale_numeric_columns(self, columns):
        self.data[columns] = self.scaler.get('standard_scaler').transform(self.data[columns])

    def encode_categorical_columns(self, columns):
        for col in columns:
            self.data[col] = self.scaler.get('label_encoders')[col].transform(self.data[col])

    def transform(self):
        # Definir os grupos de colunas
        monetary_cols = self.scaler.get('monetary_cols')
        numeric_cols = self.scaler.get('numeric_cols')
        categorical_cols = self.scaler.get('categorical_cols')

        with ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(self.input_na_numeric, monetary_cols + numeric_cols)
            executor.submit(self.input_na_categorical, categorical_cols)

        with ThreadPoolExecutor(max_workers=3) as executor:
            executor.submit(self.scale_monetary_columns, monetary_cols)
            executor.submit(self.scale_numeric_columns, numeric_cols)
            executor.submit(self.encode_categorical_columns, categorical_cols)
        return self.data
