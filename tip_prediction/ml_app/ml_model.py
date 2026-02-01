import os
import joblib
import pickle
from pathlib import Path


MODEL_PATHS = [
    # preferred path (from the notebook workspace)
    Path(__file__).resolve().parents[2] / 'ML_project' / 'models' / 'xgb_model.joblib',
    Path(__file__).resolve().parents[2] / 'ML_project' / 'models' / 'xbg_model.pkl',
]


def load_model():
    for p in MODEL_PATHS:
        if p.exists():
            try:
                if p.suffix in ['.joblib']:
                    return joblib.load(p)
                else:
                    with open(p, 'rb') as f:
                        return pickle.load(f)
            except Exception:
                continue
    raise FileNotFoundError(f"Model file not found in paths: {MODEL_PATHS}")


_MODEL = None


def get_model():
    global _MODEL
    if _MODEL is None:
        _MODEL = load_model()
    return _MODEL


def predict_tip(feature_list):
    model = get_model()
    # ensure 2D array for sklearn-like API
    arr = [feature_list]
    pred = model.predict(arr)
    try:
        return float(pred[0])
    except Exception:
        return float(pred)
