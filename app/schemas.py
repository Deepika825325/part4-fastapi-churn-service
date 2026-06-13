from enum import Enum
from typing import List

from pydantic import BaseModel, Field


class CityTier(str, Enum):
    tier1 = "Tier 1"
    tier2 = "Tier 2"
    tier3 = "Tier 3"


class AgeGroup(str, Enum):
    age_18_24 = "18-24"
    age_25_34 = "25-34"
    age_35_44 = "35-44"
    age_45_plus = "45+"


class AcquisitionChannel(str, Enum):
    organic = "Organic"
    paid = "Paid"
    referral = "Referral"
    marketplace = "Marketplace"


class LoyaltyTier(str, Enum):
    none = "None"
    silver = "Silver"
    gold = "Gold"
    platinum = "Platinum"


class PreferredCategory(str, Enum):
    skin_care = "Skin Care"
    hair_care = "Hair Care"
    wellness = "Wellness"


class MarketingConsent(str, Enum):
    yes = "Yes"
    no = "No"


class CustomerFeatures(BaseModel):
    city_tier: CityTier
    age_group: AgeGroup
    acquisition_channel: AcquisitionChannel
    loyalty_tier: LoyaltyTier
    preferred_category: PreferredCategory
    marketing_consent: MarketingConsent

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

    model_config = {
        "json_schema_extra": {
            "example": {
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
        }
    }


class BatchPredictionRequest(BaseModel):
    customers: List[CustomerFeatures] = Field(
        ...,
        min_length=1,
        max_length=1000
    )


class PredictionResponse(BaseModel):
    churn_probability: float = Field(
        ...,
        ge=0,
        le=1
    )

    predicted_class: int = Field(
        ...,
        ge=0,
        le=1
    )

    risk_level: str

    risk_explanation: str


class BatchPredictionResponse(BaseModel):
    predictions: List[PredictionResponse]