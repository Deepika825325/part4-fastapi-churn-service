from pathlib import Path

import joblib
from sklearn.pipeline import Pipeline

MODEL_PATH = Path("models/model.pkl")

_model: Pipeline | None = None


def load_model() -> Pipeline:
    global _model

    if _model is None:
        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Model file not found: {MODEL_PATH}"
            )

        _model = joblib.load(MODEL_PATH)

    return _model