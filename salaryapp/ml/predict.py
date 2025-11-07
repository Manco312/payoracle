import joblib
import os
import pandas as pd

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model_files", "model.pkl")

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Modelo no encontrado. Entrena primero con train_model.py")
    model = joblib.load(MODEL_PATH)
    return model

def predict_from_dict(input_dict):
    """
    input_dict: dict con las mismas columnas que X (age, workclass, education, education_num, ...)
    """
    model = load_model()
    df = pd.DataFrame([input_dict])
    pred = model.predict(df)[0]
    prob = model.predict_proba(df).max()
    return pred, float(prob)
