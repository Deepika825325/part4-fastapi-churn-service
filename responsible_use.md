# Responsible Use Guidelines

## Intended Use

The churn prediction API is designed to support customer retention planning by identifying customers who may be at risk of churn within the next 60 days.

The output should be used as a decision-support tool rather than an automated decision-making system.

## Appropriate Uses

* Prioritizing retention campaigns
* Identifying customers for manual review
* Supporting customer success teams
* Allocating retention budgets efficiently
* Monitoring churn trends

## Human Review Requirement

Retention teams should review high-risk customers before taking significant actions.

Business context, recent interactions, and campaign history should be considered alongside model predictions.

## Limitations

* Predictions are probabilistic estimates, not guarantees.
* Customer behavior may change rapidly after scoring.
* The model may not capture all external factors influencing churn.
* Prediction quality may degrade if customer behavior changes significantly over time.

## Prohibited Uses

The API should not be used for:

* Fully automated customer decisions
* Denial of service or support access
* Discriminatory treatment of customers
* Decisions unrelated to customer retention

## Fairness Considerations

Teams should regularly review model performance across different customer groups to identify potential biases and unintended impacts.

## Escalation Process

If unusual prediction behavior is observed, the retention team should notify the analytics team for investigation and potential model retraining.
