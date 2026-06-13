import logging
from typing import List

import pandas as pd

from app.model_loader import load_model
from app.risk_explainer import generate_risk_explanation
from app.schemas import (
    CustomerFeatures,
    PredictionResponse
)

logger = logging.getLogger(__name__)

CHURN_THRESHOLD = 0.45
HIGH_RISK_THRESHOLD = 0.75

model = load_model()


def get_risk_level(
    churn_probability: float
) -> str:

    if churn_probability >= HIGH_RISK_THRESHOLD:
        return "high"

    if churn_probability >= CHURN_THRESHOLD:
        return "medium"

    return "low"


def predict_single(
    customer: CustomerFeatures
) -> PredictionResponse:

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

    logger.info(
        "Prediction generated | probability=%.4f | class=%s",
        churn_probability,
        predicted_class
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

    customer_df = pd.DataFrame(
        [
            customer.model_dump()
            for customer in customers
        ]
    )

    probabilities = model.predict_proba(
        customer_df
    )[:, 1]

    predictions = []

    for customer, probability in zip(
        customers,
        probabilities
    ):

        probability = float(
            probability
        )

        predicted_class = int(
            probability >= CHURN_THRESHOLD
        )

        risk_level = get_risk_level(
            probability
        )

        risk_explanation = generate_risk_explanation(
            customer,
            risk_level
        )

        predictions.append(
            PredictionResponse(
                churn_probability=round(
                    probability,
                    4
                ),
                predicted_class=predicted_class,
                risk_level=risk_level,
                risk_explanation=risk_explanation
            )
        )

    logger.info(
        "Batch prediction completed for %s customers",
        len(customers)
    )

    return predictions