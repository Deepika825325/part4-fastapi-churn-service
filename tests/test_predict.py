from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_predict():

    payload = {
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

    response = client.post(
        "/predict",
        json=payload
    )

    assert response.status_code == 200

    data = response.json()

    assert "churn_probability" in data
    assert "predicted_class" in data
    assert "risk_level" in data
    assert "risk_explanation" in data