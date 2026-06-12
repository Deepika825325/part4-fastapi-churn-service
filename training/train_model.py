import pandas as pd
import joblib

from pathlib import Path

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

DATA_PATH = "data/rfm_modeling_snapshot.csv"
MODEL_PATH = "models/model.pkl"

df = pd.read_csv(DATA_PATH)

target = "churn_next_60d"

drop_cols = [
    "customer_id",
    "snapshot_date",
    "split",
    target
]

X = df.drop(columns=drop_cols)
y = df[target]

categorical_features = [
    "city_tier",
    "age_group",
    "acquisition_channel",
    "loyalty_tier",
    "preferred_category",
    "marketing_consent"
]

numeric_features = [
    col for col in X.columns
    if col not in categorical_features
]

numeric_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]
)

categorical_transformer = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore"
            )
        )
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        (
            "num",
            numeric_transformer,
            numeric_features
        ),
        (
            "cat",
            categorical_transformer,
            categorical_features
        )
    ]
)

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "classifier",
            LogisticRegression(
                max_iter=5000,
                random_state=42
            )
        )
    ]
)

pipeline.fit(X, y)

Path("models").mkdir(
    exist_ok=True
)

joblib.dump(
    pipeline,
    MODEL_PATH
)

print(
    f"Model saved to {MODEL_PATH}"
)