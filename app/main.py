import logging

from fastapi import FastAPI, HTTPException

from app.predictor import predict_batch, predict_single
from app.schemas import (
    BatchPredictionRequest,
    BatchPredictionResponse,
    CustomerFeatures,
    PredictionResponse,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(
    title="D2C Churn Prediction API",
    version="1.0.0",
    description="Customer churn prediction service for CRM and retention workflows."
)


@app.get("/", tags=["System"])
def root():
    return {
        "service": "D2C Churn Prediction API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health", tags=["System"])
def health():
    return {
        "status": "ok"
    }


@app.post(
    "/predict",
    response_model=PredictionResponse,
    tags=["Prediction"],
    summary="Predict churn risk for a single customer"
)
def predict(customer: CustomerFeatures):
    try:
        logger.info(
            "Single prediction request received"
        )

        return predict_single(customer)

    except Exception:
        logger.exception(
            "Prediction request failed"
        )

        raise HTTPException(
            status_code=500,
            detail="Prediction service error"
        )


@app.post(
    "/batch_predict",
    response_model=BatchPredictionResponse,
    tags=["Prediction"],
    summary="Predict churn risk for multiple customers"
)
def batch_predict_endpoint(
    request: BatchPredictionRequest
):
    try:
        logger.info(
            "Batch prediction request received for %s customers",
            len(request.customers)
        )

        predictions = predict_batch(
            request.customers
        )

        return BatchPredictionResponse(
            predictions=predictions
        )

    except Exception:
        logger.exception(
            "Batch prediction request failed"
        )

        raise HTTPException(
            status_code=500,
            detail="Prediction service error"
        )