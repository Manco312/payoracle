# Ejecutar localmente: python salaryapp/ml/train_model.py --data_path path/to/adult.csv
import argparse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from imblearn.over_sampling import SMOTENC
import joblib
import os

def load_and_clean(path):
    datos = pd.read_csv(path)
    datos = datos.replace('?', pd.NA)
    datos = datos.replace(r'^\s*$', pd.NA, regex=True)
    datos = datos.dropna()
    # Aseguramos nombres de columnas consistentes (si vienen con puntos o espacios)
    datos.columns = [c.strip() for c in datos.columns]
    return datos

def main(data_path, out_dir="model_files"):
    os.makedirs(out_dir, exist_ok=True)
    datos = load_and_clean(data_path)

    # target
    X = datos.drop(columns=["income", "fnlwgt"], errors='ignore')
    y = datos["income"]

    # split
    X_train, X_temp, y_train, y_temp = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y
    )
    X_val, X_test, y_val, y_test = train_test_split(
        X_temp, y_temp, test_size=0.50, random_state=42, stratify=y_temp
    )

    # detectar categóricas en X_train
    columnas_categoricas = X_train.select_dtypes(include=["object", "category"]).columns.tolist()
    cat_indices = [X_train.columns.get_loc(c) for c in columnas_categoricas]

    # SMOTENC (solo sobre X_train)
    sm = SMOTENC(categorical_features=cat_indices, random_state=42)
    X_train_res, y_train_res = sm.fit_resample(X_train, y_train)

    # definir preprocesador
    num_cols = X_train_res.select_dtypes(include=np.number).columns.tolist()
    cat_cols = X_train_res.select_dtypes(exclude=np.number).columns.tolist()

    preprocessor = ColumnTransformer([
        ("num", StandardScaler(), num_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore", sparse_output=False), cat_cols)
    ], remainder='drop')

    # pipeline con RF (puedes probar GB también)
    pipeline = Pipeline([
        ("pre", preprocessor),
        ("clf", RandomForestClassifier(random_state=42, n_jobs=-1))
    ])

    param_grid = {
        "clf__n_estimators": [100],
        "clf__max_depth": [5, 7, None]
    }

    gs = GridSearchCV(pipeline, param_grid=param_grid, cv=3, n_jobs=-1)
    gs.fit(X_train_res, y_train_res)

    print("Mejor score CV:", gs.best_score_)
    print("Mejores params:", gs.best_params_)

    # Guardar el modelo completo (incluye el preprocesador)
    model_path = os.path.join(out_dir, "model.pkl")
    joblib.dump(gs.best_estimator_, model_path)
    print("Modelo guardado en:", model_path)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--data_path", required=True)
    p.add_argument("--out_dir", default="model_files")
    args = p.parse_args()
    main(args.data_path, args.out_dir)
