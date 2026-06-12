from fastapi import FastAPI, HTTPException

from app.predictor import (
    predict_single,
    predict_batch
)

from app.schemas import (
    CustomerFeatures,
    BatchPredictionRequest,
    PredictionResponse,
    BatchPredictionResponse
)

app = FastAPI(
    title="D2C Churn Prediction API",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {
        "status": "ok"
    }


@app.post(
    "/predict",
    response_model=PredictionResponse
)
def predict(
    customer: CustomerFeatures
):
    try:
        return predict_single(customer)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


@app.post(
    "/batch_predict",
    response_model=BatchPredictionResponse
)
def batch_predict_endpoint(
    request: BatchPredictionRequest
):
    try:
        predictions = predict_batch(
            request.customers
        )

        return {
            "predictions": predictions
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )