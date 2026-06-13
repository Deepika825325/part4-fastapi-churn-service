# streamlit_app.py

import json
import requests
import pandas as pd
import streamlit as st

API_URL = "https://part4-fastapi-churn-service-production.up.railway.app"

st.set_page_config(
    page_title="D2C Customer Churn Prediction",
    page_icon="📊",
    layout="wide"
)

st.markdown(
    """
    <style>
    .main {
        background-color: #f5f6f8;
    }

    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
    }

    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e5e7eb;
    }

    div[data-testid="metric-container"] {
        background-color: white;
        border: 1px solid #e5e7eb;
        padding: 12px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

if "history" not in st.session_state:
    st.session_state.history = []

st.title("D2C Customer Churn Prediction Dashboard")

st.caption(
    "Predict customer churn risk using a trained machine learning model and FastAPI scoring service."
)

sidebar = st.sidebar

sidebar.title("Navigation")
sidebar.markdown("### Single Prediction")
sidebar.markdown("### Batch Prediction")
sidebar.markdown("### Prediction History")
sidebar.divider()

try:
    health_response = requests.get(
        f"{API_URL}/health",
        timeout=5
    )

    if health_response.status_code == 200:
        sidebar.success("API Connected")
    else:
        sidebar.error("API Unavailable")

except Exception:
    sidebar.error("API Offline")

sidebar.info("Model: Logistic Regression")
sidebar.info("Threshold: 0.45")

tab1, tab2 = st.tabs(
    [
        "Single Customer Prediction",
        "Batch Prediction"
    ]
)

with tab1:

    left_col, right_col = st.columns([2, 1])

    with left_col:

        st.subheader("Customer Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            city_tier = st.selectbox(
                "City Tier",
                ["Tier 1", "Tier 2", "Tier 3"]
            )

        with col2:
            age_group = st.selectbox(
                "Age Group",
                ["18-24", "25-34", "35-44", "45+"]
            )

        with col3:
            acquisition_channel = st.selectbox(
                "Acquisition Channel",
                ["Organic", "Marketplace", "Referral", "Paid"]
            )

        col1, col2, col3 = st.columns(3)

        with col1:
            loyalty_tier = st.selectbox(
                "Loyalty Tier",
                ["None", "Silver", "Gold", "Platinum"]
            )

        with col2:
            preferred_category = st.selectbox(
                "Preferred Category",
                ["Skin Care", "Hair Care", "Wellness"]
            )

        with col3:
            marketing_consent = st.selectbox(
                "Marketing Consent",
                ["Yes", "No"]
            )

        st.subheader("Behavioral Metrics")

        col1, col2, col3 = st.columns(3)

        with col1:
            recency_days = st.number_input(
                "Recency Days",
                min_value=0,
                value=30
            )

            return_rate_180d = st.number_input(
                "Return Rate",
                min_value=0.0,
                max_value=1.0,
                value=0.05
            )

            category_diversity_180d = st.number_input(
                "Category Diversity",
                min_value=0,
                value=3
            )

            avg_resolution_hours_90d = st.number_input(
                "Resolution Hours",
                min_value=0,
                value=12
            )

        with col2:
            frequency_180d = st.number_input(
                "Frequency (180d)",
                min_value=0,
                value=5
            )

            avg_discount_pct_180d = st.number_input(
                "Average Discount %",
                min_value=0.0,
                max_value=1.0,
                value=0.10
            )

            ticket_count_90d = st.number_input(
                "Ticket Count",
                min_value=0,
                value=1
            )

            days_since_signup = st.number_input(
                "Days Since Signup",
                min_value=0,
                value=400
            )

        with col3:
            monetary_180d = st.number_input(
                "Monetary Value",
                min_value=0.0,
                value=5000.0
            )

            avg_rating_180d = st.number_input(
                "Average Rating",
                min_value=0.0,
                max_value=5.0,
                value=4.2
            )

            negative_ticket_rate_90d = st.number_input(
                "Negative Ticket Rate",
                min_value=0.0,
                max_value=1.0,
                value=0.10
            )

            last_visit_days_ago = st.number_input(
                "Last Visit Days Ago",
                min_value=0,
                value=3
            )

        st.subheader("Engagement Metrics")

        col1, col2, col3 = st.columns(3)

        with col1:
            sessions_30d = st.number_input(
                "Sessions",
                min_value=0,
                value=15
            )

            abandoned_carts_30d = st.number_input(
                "Abandoned Carts",
                min_value=0,
                value=1
            )

        with col2:
            product_views_30d = st.number_input(
                "Product Views",
                min_value=0,
                value=50
            )

            email_opens_30d = st.number_input(
                "Email Opens",
                min_value=0,
                value=5
            )

        with col3:
            cart_adds_30d = st.number_input(
                "Cart Adds",
                min_value=0,
                value=8
            )

            campaign_clicks_30d = st.number_input(
                "Campaign Clicks",
                min_value=0,
                value=2
            )

        wishlist_adds_30d = st.number_input(
            "Wishlist Adds",
            min_value=0,
            value=4
        )

        predict_clicked = st.button(
            "Predict Churn Risk",
            use_container_width=True
        )

    payload = {
        "city_tier": city_tier,
        "age_group": age_group,
        "acquisition_channel": acquisition_channel,
        "loyalty_tier": loyalty_tier,
        "preferred_category": preferred_category,
        "marketing_consent": marketing_consent,
        "recency_days": recency_days,
        "frequency_180d": frequency_180d,
        "monetary_180d": monetary_180d,
        "return_rate_180d": return_rate_180d,
        "avg_discount_pct_180d": avg_discount_pct_180d,
        "avg_rating_180d": avg_rating_180d,
        "category_diversity_180d": category_diversity_180d,
        "ticket_count_90d": ticket_count_90d,
        "negative_ticket_rate_90d": negative_ticket_rate_90d,
        "avg_resolution_hours_90d": avg_resolution_hours_90d,
        "days_since_signup": days_since_signup,
        "sessions_30d": sessions_30d,
        "product_views_30d": product_views_30d,
        "cart_adds_30d": cart_adds_30d,
        "wishlist_adds_30d": wishlist_adds_30d,
        "abandoned_carts_30d": abandoned_carts_30d,
        "email_opens_30d": email_opens_30d,
        "campaign_clicks_30d": campaign_clicks_30d,
        "last_visit_days_ago": last_visit_days_ago
    }

    with right_col:

        st.subheader("Prediction Result")

        if predict_clicked:

            try:
                response = requests.post(
                    f"{API_URL}/predict",
                    json=payload,
                    timeout=10
                )

                if response.status_code == 200:

                    result = response.json()

                    st.metric(
                        "Churn Probability",
                        f"{result['churn_probability']:.2%}"
                    )

                    st.progress(
                        float(result["churn_probability"])
                    )

                    st.metric(
                        "Risk Level",
                        result["risk_level"].title()
                    )

                    st.info(
                        result["risk_explanation"]
                    )

                    st.session_state.history.append(
                        result
                    )

                    st.download_button(
                        label="Download Prediction Report",
                        data=json.dumps(
                            result,
                            indent=4
                        ),
                        file_name="prediction_report.json",
                        mime="application/json"
                    )

            except Exception as e:
                st.error(
                    f"API Connection Error: {e}"
                )

with tab2:

    st.subheader("Batch Prediction")

    uploaded_file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if uploaded_file:

        df = pd.read_csv(
            uploaded_file
        )

        st.dataframe(df.head())

        if st.button(
            "Run Batch Prediction"
        ):

            customers = df.to_dict(
                orient="records"
            )

            response = requests.post(
                f"{API_URL}/batch_predict",
                json={
                    "customers": customers
                }
            )

            if response.status_code == 200:
                st.success(
                    "Batch prediction completed."
                )

                st.json(
                    response.json()
                )

if st.session_state.history:

    st.divider()

    st.subheader("Prediction History")

    st.dataframe(
        pd.DataFrame(
            st.session_state.history
        ),
        use_container_width=True
    )