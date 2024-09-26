from src.use_cases.application_score.predict import Runner
import pandas as pd
from sklearn.metrics import accuracy_score


def test_application_score():
    data = pd.read_csv('')
    runner = Runner(data)
    classify = runner.execute()
    threshold = 0.5
    y_pred = (classify.prob >= threshold).astype(int)
    accuracy = accuracy_score(data['default'], y_pred)
    assert accuracy > 0.7

