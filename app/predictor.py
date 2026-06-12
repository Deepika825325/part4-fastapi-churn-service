from typing import List

import pandas as pd

from app.model_loader import load_model
from app.risk_explainer import generate_risk_explanation
from app.schemas import (
    CustomerFeatures,
    PredictionResponse
)

CHURN_THRESHOLD = 0.45


def get_risk_level(
    churn_probability: float
) -> str:

    if churn_probability >= 0.70:
        return "high"

    if churn_probability >= 0.40:
        return "medium"

    return "low"


def predict_single(
    customer: CustomerFeatures
) -> PredictionResponse:

    model = load_model()

    customer_df = pd.DataFrame(
        [customer.model_dump()]
    )

    churn_probability = float(
        model.predict_proba(customer_df)[0][1]
    )

    predicted_class = int(
        churn_probability >= CHURN_THRESHOLD
    )

    risk_level = get_risk_level(
        churn_probability
    )

    risk_explanation = generate_risk_explanation(
        customer,
        risk_level
    )

    return PredictionResponse(
        churn_probability=round(
            churn_probability,
            4
        ),
        predicted_class=predicted_class,
        risk_level=risk_level,
        risk_explanation=risk_explanation
    )


def predict_batch(
    customers: List[CustomerFeatures]
) -> List[PredictionResponse]:

    return [
        predict_single(customer)
        for customer in customers
    ]