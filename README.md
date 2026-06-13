# D2C Customer Churn Prediction API

## Overview

This project implements a production-ready FastAPI service for predicting customer churn risk for a Direct-to-Consumer (D2C) personal care brand.

The service loads a trained machine learning model, accepts customer behavioral and engagement features, and returns:

* Churn probability
* Predicted churn class
* Risk level
* Human-readable risk explanation

The API is intended for internal CRM and retention teams to prioritize customer retention efforts and support data-driven decision making.

---

## Project Structure

```text
part4-fastapi-churn-service/

app/
├── __init__.py
├── main.py
├── model_loader.py
├── predictor.py
├── risk_explainer.py
└── schemas.py

training/
└── train_model.py

models/
└── model.pkl

tests/
├── test_health.py
├── test_predict.py
└── test_batch_predict.py

sample_requests/
├── single_customer.json
└── batch_customers.json

monitoring_plan.md
responsible_use.md
requirements.txt
Dockerfile
README.md
.gitignore
```

---

## Model Information

### Objective

Predict whether a customer is likely to churn within the next 60 days.

### Algorithm

* Logistic Regression
* Scikit-Learn Pipeline
* OneHotEncoder for categorical features
* StandardScaler for numerical features

### Decision Threshold

The API uses a churn classification threshold of:

```text
0.45
```

This threshold was selected during model evaluation to balance precision and recall for retention use cases.

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd part4-fastapi-churn-service
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Training the Model

To regenerate the trained model artifact:

```bash
python training/train_model.py
```

This creates:

```text
models/model.pkl
```

---

## Running the API

Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

API URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

ReDoc Documentation:

```text
http://127.0.0.1:8000/redoc
```

---

## API Endpoints

### GET /health

Health check endpoint.

#### Response

```json
{
  "status": "ok"
}
```

---

### POST /predict

Returns churn prediction for a single customer.

#### Sample Request

```json
{
  "city_tier": "Tier 1",
  "age_group": "25-34",
  "acquisition_channel": "Organic",
  "loyalty_tier": "Gold",
  "preferred_category": "Skin Care",
  "marketing_consent": "Yes",
  "recency_days": 30,
  "frequency_180d": 5,
  "monetary_180d": 5000,
  "return_rate_180d": 0.05,
  "avg_discount_pct_180d": 0.10,
  "avg_rating_180d": 4.2,
  "category_diversity_180d": 3,
  "ticket_count_90d": 1,
  "negative_ticket_rate_90d": 0.10,
  "avg_resolution_hours_90d": 12,
  "days_since_signup": 400,
  "sessions_30d": 15,
  "product_views_30d": 50,
  "cart_adds_30d": 8,
  "wishlist_adds_30d": 4,
  "abandoned_carts_30d": 1,
  "email_opens_30d": 5,
  "campaign_clicks_30d": 2,
  "last_visit_days_ago": 3
}
```

#### Sample Response

```json
{
  "churn_probability": 0.0053,
  "predicted_class": 0,
  "risk_level": "low",
  "risk_explanation": "Customer demonstrates healthy engagement, purchasing activity, and overall behavioral patterns associated with low churn risk."
}
```

---

### POST /batch_predict

Returns churn predictions for multiple customers.

#### Sample Request

```json
{
  "customers": [
    {
      "...": "customer_1_features"
    },
    {
      "...": "customer_2_features"
    }
  ]
}
```

#### Sample Response

```json
{
  "predictions": [
    {
      "churn_probability": 0.12,
      "predicted_class": 0,
      "risk_level": "low",
      "risk_explanation": "..."
    },
    {
      "churn_probability": 0.84,
      "predicted_class": 1,
      "risk_level": "high",
      "risk_explanation": "..."
    }
  ]
}
```

---

## Running Tests

Execute all API tests:

```bash
pytest
```

Expected result:

```text
3 passed
```

Test Coverage:

* Health endpoint
* Single prediction endpoint
* Batch prediction endpoint

---

## Docker Usage

### Build Image

```bash
docker build -t churn-api .
```

### Run Container

```bash
docker run -p 8000:8000 churn-api
```

API will be available at:

```text
http://localhost:8000
```

---

## Monitoring

The deployment monitoring plan is documented in:

```text
monitoring_plan.md
```

The monitoring strategy covers:

* Data drift detection
* Prediction distribution tracking
* Business outcome monitoring
* API reliability monitoring
* Retraining triggers

---

## Responsible Use

Responsible usage guidelines are documented in:

```text
responsible_use.md
```

Key principles:

* Predictions support human decision making
* Predictions should not be used as the sole basis for customer actions
* High-risk customers should be reviewed before intervention
* Regular fairness and performance reviews should be conducted

---

## Dataset Notes

This project uses the modeling snapshot dataset provided as part of the capstone project.

Only customer information available at or before the snapshot date is used for prediction to prevent data leakage.

The API is designed as a reproducible scoring service and can retrain the model using the provided training script.

---

## Author
Deepika Kumari

Capstone Project – D2C Customer Churn Intelligence & Retention API

Part 4: FastAPI Churn Scoring Service & Reproducible ML Workflow
