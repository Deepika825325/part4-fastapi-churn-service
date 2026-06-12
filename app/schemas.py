from typing import List

from pydantic import BaseModel, Field


class CustomerFeatures(BaseModel):
    city_tier: str
    age_group: str
    acquisition_channel: str
    loyalty_tier: str | None = None
    preferred_category: str
    marketing_consent: str

    recency_days: float = Field(..., ge=0)
    frequency_180d: float = Field(..., ge=0)
    monetary_180d: float = Field(..., ge=0)

    return_rate_180d: float = Field(..., ge=0, le=1)
    avg_discount_pct_180d: float = Field(..., ge=0, le=1)

    avg_rating_180d: float = Field(..., ge=0, le=5)

    category_diversity_180d: float = Field(..., ge=0)

    ticket_count_90d: int = Field(..., ge=0)

    negative_ticket_rate_90d: float = Field(..., ge=0, le=1)

    avg_resolution_hours_90d: float = Field(..., ge=0)

    days_since_signup: int = Field(..., ge=0)

    sessions_30d: int = Field(..., ge=0)
    product_views_30d: int = Field(..., ge=0)
    cart_adds_30d: int = Field(..., ge=0)
    wishlist_adds_30d: int = Field(..., ge=0)
    abandoned_carts_30d: int = Field(..., ge=0)

    email_opens_30d: int = Field(..., ge=0)
    campaign_clicks_30d: int = Field(..., ge=0)

    last_visit_days_ago: int = Field(..., ge=0)


class BatchPredictionRequest(BaseModel):
    customers: List[CustomerFeatures]


class PredictionResponse(BaseModel):
    churn_probability: float
    predicted_class: int
    risk_level: str
    risk_explanation: str


class BatchPredictionResponse(BaseModel):
    predictions: List[PredictionResponse]