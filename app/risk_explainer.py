from app.schemas import CustomerFeatures


def generate_risk_explanation(
    customer: CustomerFeatures,
    risk_level: str
) -> str:

    risk_factors = []

    if customer.recency_days > 60:
        risk_factors.append("long time since last purchase")

    if customer.frequency_180d < 3:
        risk_factors.append("low purchase frequency")

    if customer.monetary_180d < 1000:
        risk_factors.append("low recent spending")

    if customer.sessions_30d < 5:
        risk_factors.append("low platform engagement")

    if customer.product_views_30d < 10:
        risk_factors.append("limited browsing activity")

    if customer.email_opens_30d < 2:
        risk_factors.append("low marketing engagement")

    if customer.last_visit_days_ago > 30:
        risk_factors.append("infrequent recent visits")

    if customer.ticket_count_90d >= 3:
        risk_factors.append("high support ticket volume")

    if customer.negative_ticket_rate_90d > 0.30:
        risk_factors.append("negative support experience")

    if customer.avg_resolution_hours_90d > 48:
        risk_factors.append("slow issue resolution")

    if customer.return_rate_180d > 0.30:
        risk_factors.append("high product return rate")

    if customer.abandoned_carts_30d >= 3:
        risk_factors.append("frequent cart abandonment")

    if risk_level == "low":
        return (
            "Customer demonstrates healthy engagement, purchasing activity, "
            "and overall behavioral patterns associated with low churn risk."
        )

    if not risk_factors:
        return (
            "The model identified churn-related patterns, although no single "
            "dominant business risk factor was detected."
        )

    if len(risk_factors) == 1:
        return (
            f"Churn risk is influenced primarily by {risk_factors[0]}."
        )

    if len(risk_factors) == 2:
        return (
            f"Churn risk is influenced by {risk_factors[0]} "
            f"and {risk_factors[1]}."
        )

    top_factors = risk_factors[:4]

    return (
        "Churn risk is influenced by "
        + ", ".join(top_factors[:-1])
        + f", and {top_factors[-1]}."
    )