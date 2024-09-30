import pandas as pd
import pickle
from sklearn.metrics import accuracy_score


def test_application_score_2():
    data = pd.read_csv('tests/use_cases/application_score/predict/data/base_test.csv')

    filename = 'src/use_cases/application_score/models/model_.pkl'
    with open(filename, 'rb') as file:
        model = pickle.load(file)

    threshold = 0.5
    prob = model.predict_proba(data.get(model.feature_names_in_))[:, 1]
    y_pred = (prob >= threshold).astype(int)
    accuracy = accuracy_score(data['default'], y_pred)
    assert accuracy > 0.7
