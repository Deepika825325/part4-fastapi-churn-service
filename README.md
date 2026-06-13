# D2C Customer Churn Prediction API

## Overview

A production-ready FastAPI service for customer churn prediction, developed as part of the **D2C Customer Churn Intelligence & Retention API Capstone Project**.

The application exposes REST API endpoints that allow CRM, retention, and marketing systems to score customers for churn risk, generate interpretable risk explanations, and support targeted customer retention initiatives.

The project includes:

* FastAPI prediction service
* Scikit-Learn churn prediction model
* Batch prediction support
* Pydantic validation
* Automated API testing
* Dockerized deployment
* Streamlit dashboard
* Monitoring strategy
* Responsible-use guidelines

---
## Live Demo

### Streamlit Dashboard

https://part4-fastapi-churn-service-exrsx3v2ufpswkj82kkdws.streamlit.app/

### FastAPI API

https://part4-fastapi-churn-service-production.up.railway.app

### Swagger Documentation

https://part4-fastapi-churn-service-production.up.railway.app/docs

### ReDoc Documentation

https://part4-fastapi-churn-service-production.up.railway.app/redoc

### Health Check

https://part4-fastapi-churn-service-production.up.railway.app/health

### Quick Evaluation

Evaluators can test the deployed application without local installation:

1. Open the Streamlit Dashboard.
2. Generate churn predictions using the user interface.
3. Upload the sample batch CSV file.
4. Test API endpoints through Swagger UI.
5. Verify deployment status using the health endpoint.
---
## Key Features

* Single customer churn prediction
* Batch churn prediction
* Probability-based risk scoring
* Human-readable churn explanations
* Strong input validation using Pydantic
* Enum validation for categorical features
* Automated API testing with Pytest
* Docker support for reproducible deployment
* Streamlit-based user interface
* Reproducible model training workflow
* Monitoring and governance documentation

---

## Technology Stack

* Python 3.13
* FastAPI
* Scikit-Learn
* Pandas
* NumPy
* Pydantic
* Uvicorn
* Pytest
* Streamlit
* Docker

---

## Repository Structure

```text
part4-fastapi-churn-service/
│
├── app/
│   ├── main.py
│   ├── model_loader.py
│   ├── predictor.py
│   ├── risk_explainer.py
│   └── schemas.py
│
├── models/
│   └── model.pkl
│
├── training/
│   └── train_model.py
│
├── tests/
│   ├── conftest.py
│   ├── test_health.py
│   ├── test_predict.py
│   ├── test_batch_predict.py
│   ├── test_validation.py
│   └── test_risk_level.py
│
├──  sample_requests/
|   ├── single_customer.json
|   ├── batch_customers.json
|   └── churn_batch_examples.csv
│
├── streamlit_app.py
├── monitoring_plan.md
├── responsible_use.md
├── requirements.txt
├── Dockerfile
├── pytest.ini
├── .gitignore
└── README.md
```
---
## Business Objective

The company wants to identify customers who are likely to churn within the next 60 days and prioritize retention efforts efficiently.

The API provides:

* Churn probability
* Churn classification
* Risk level
* Business-friendly explanation

These outputs support CRM workflows, customer success teams, and retention campaigns.

---

## System Architecture

```text
Streamlit Dashboard
        │
        ▼
FastAPI Service
        │
        ▼
Pydantic Validation
        │
        ▼
Prediction Engine
        │
        ▼
Scikit-Learn Pipeline
        │
        ▼
Risk Explanation Engine
        │
        ▼
JSON Response
```

---

## Model Information

### Prediction Target

Predict whether a customer is likely to churn within the next 60 days.

### Model

* Logistic Regression
* Scikit-Learn Pipeline
* OneHotEncoder
* StandardScaler

### Churn Classification Threshold

```text
0.45
```

The threshold was selected during model evaluation to balance precision and recall for retention-focused business decisions.

---

## Risk Level Definitions

| Risk Level | Probability Range |
| ---------- | ----------------- |
| Low        | < 0.45            |
| Medium     | 0.45 – 0.74       |
| High       | ≥ 0.75            |

Customers classified as Medium or High Risk are assigned:

```text
predicted_class = 1
```

Customers classified as Low Risk are assigned:

```text
predicted_class = 0
```

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

### Activate Environment

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

To regenerate the model artifact:

```bash
python training/train_model.py
```

Generated artifact:

```text
models/model.pkl
```

---

## Running the FastAPI Service

Start the API server:

```bash
uvicorn app.main:app --reload
```

Available URLs:

```text
API Base URL
http://127.0.0.1:8000

Swagger UI
http://127.0.0.1:8000/docs

ReDoc
http://127.0.0.1:8000/redoc
```

---

## Running the Streamlit Dashboard

```bash
streamlit run streamlit_app.py
```

Application URL:

```text
http://localhost:8501
```

The dashboard connects directly to the FastAPI prediction service.

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

### Sample Batch Prediction File

A sample CSV file is included for testing batch predictions:

sample_requests/churn_batch_examples.csv

The file contains example low-risk, medium-risk, and high-risk customers and can be uploaded directly through the Streamlit Batch Prediction interface.

This allows evaluators to quickly validate:

* Batch prediction functionality
* Input validation
* Risk classification logic
* API response structure

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
  "churn_probability": 0.053,
  "predicted_class": 0,
  "risk_level": "low",
  "risk_explanation": "Customer demonstrates strong engagement, healthy purchasing behavior, and no significant churn warning signals."
}
```

---

### Response Fields

| Field             | Description                    |
| ----------------- | ------------------------------ |
| churn_probability | Predicted probability of churn |
| predicted_class   | Binary churn classification    |
| risk_level        | Low, Medium, or High           |
| risk_explanation  | Human-readable explanation     |

---

### POST /batch_predict

Returns predictions for multiple customers.

#### Response Structure

```json
{
  "predictions": [
    {
      "churn_probability": 0.48,
      "predicted_class": 1,
      "risk_level": "medium",
      "risk_explanation": "..."
    }
  ]
}
```

---

## Testing

Run the complete test suite:

```bash
pytest
```

Expected result:

```text
12 passed
```

### Test Coverage

* Health endpoint
* Single prediction endpoint
* Batch prediction endpoint
* Input validation
* Enum validation
* Numeric boundary validation
* Risk threshold validation
* Business rule validation

---

## Docker Deployment

### Build Docker Image

```bash
docker build -t churn-api .
```

### Run Docker Container

```bash
docker run -p 8000:8000 churn-api
```

API URL:

```text
http://localhost:8000
```

---

## Monitoring

Deployment monitoring strategy is documented in:

```text
monitoring_plan.md
```

Monitoring covers:

* Data drift detection
* Prediction distribution monitoring
* Model performance tracking
* Business outcome monitoring
* API reliability monitoring
* Retraining triggers

---

## Responsible Use

Responsible-use guidance is documented in:

```text
responsible_use.md
```

Key principles:

* Human-in-the-loop decision making
* Predictions support, not replace, business judgment
* Fair and ethical customer treatment
* Awareness of model limitations
* Review of high-risk recommendations before action

---

## Reproducibility

This repository is fully reproducible.

Install dependencies:

```bash
pip install -r requirements.txt
```

Retrain the model:

```bash
python training/train_model.py
```

Run the API:

```bash
uvicorn app.main:app --reload
```

Run tests:

```bash
pytest
```

Run Streamlit:

```bash
streamlit run streamlit_app.py
```

---

## Dataset Notes

This project uses the modeling snapshot dataset provided as part of the capstone dataset package.

Only customer information available on or before the snapshot date was used during feature engineering and model training.

No post-snapshot information was used, preventing target leakage and ensuring realistic deployment behavior.

---

## Author

**Deepika Kumari**

Capstone Project

**D2C Customer Churn Intelligence & Retention API**

Part 4: FastAPI Churn Scoring Service & Reproducible ML Workflow
