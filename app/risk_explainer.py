from app.schemas import CustomerFeatures


def generate_risk_explanation(
    customer: CustomerFeatures,
    risk_level: str
) -> str:

    risk_factors = []

    if customer.recency_days > 60:
        risk_factors.append(
            "extended time since the last purchase"
        )

    if customer.frequency_180d < 3:
        risk_factors.append(
            "low purchase frequency"
        )

    if customer.monetary_180d < 1000:
        risk_factors.append(
            "low recent spending activity"
        )

    if customer.sessions_30d < 5:
        risk_factors.append(
            "low platform engagement"
        )

    if customer.product_views_30d < 10:
        risk_factors.append(
            "limited product browsing activity"
        )

    if customer.email_opens_30d < 2:
        risk_factors.append(
            "low marketing engagement"
        )

    if customer.last_visit_days_ago > 30:
        risk_factors.append(
            "infrequent recent visits"
        )

    if customer.ticket_count_90d >= 3:
        risk_factors.append(
            "high support ticket volume"
        )

    if customer.negative_ticket_rate_90d > 0.30:
        risk_factors.append(
            "negative support experiences"
        )

    if customer.avg_resolution_hours_90d > 48:
        risk_factors.append(
            "slow support issue resolution"
        )

    if customer.return_rate_180d > 0.30:
        risk_factors.append(
            "high product return rate"
        )

    if customer.abandoned_carts_30d >= 3:
        risk_factors.append(
            "frequent cart abandonment"
        )

    if risk_level == "low":

        if not risk_factors:
            return (
                "Customer demonstrates strong engagement, healthy purchasing behavior, "
                "and no significant churn warning signals."
            )

        return (
            "Customer is currently classified as low risk. Minor warning signals were "
            f"detected, including {', '.join(risk_factors[:2])}."
        )

    if risk_level == "medium":

        if not risk_factors:
            return (
                "The model detected moderate churn-related behavioral patterns that "
                "should be monitored."
            )

        top_factors = risk_factors[:3]

        return (
            "Moderate churn risk is associated with "
            + ", ".join(top_factors[:-1])
            + f", and {top_factors[-1]}. "
            "Targeted retention engagement is recommended."
        )

    if not risk_factors:
        return (
            "The model detected significant churn-related behavioral patterns. "
            "Customer retention intervention is recommended."
        )

    top_factors = risk_factors[:4]

    return (
        "High churn risk is primarily driven by "
        + ", ".join(top_factors[:-1])
        + f", and {top_factors[-1]}. "
        "Immediate retention intervention is recommended."
    )