# Monitoring Plan

## Objective

The D2C Customer Churn Prediction API supports retention decision-making by estimating the probability that a customer will churn within the next 60 days. Continuous monitoring is required to ensure prediction quality, system reliability, and business impact.

## 1. Data Drift Monitoring

Monitor whether incoming customer data differs significantly from the data used during model training.

Key features to monitor:

* recency_days
* frequency_180d
* monetary_180d
* sessions_30d
* product_views_30d
* ticket_count_90d
* return_rate_180d

Metrics:

* Population Stability Index (PSI)
* Distribution comparisons
* Missing value rates
* Category frequency changes

Alert Threshold:

* PSI > 0.25 for any critical feature

## 2. Prediction Distribution Monitoring

Track model output distributions over time.

Metrics:

* Average churn probability
* Percentage of customers classified as high risk
* Percentage of customers classified as medium risk
* Percentage of customers classified as low risk

Alert Thresholds:

* Sudden changes greater than 20% from historical averages
* Large shifts in prediction distributions

## 3. Business Outcome Monitoring

Compare predictions with actual customer outcomes.

Metrics:

* Retention campaign conversion rate
* Actual churn rate
* Precision
* Recall
* F1 Score
* ROC-AUC

Business KPIs:

* Reduction in churn rate
* Revenue retained
* Campaign ROI

## 4. API Reliability Monitoring

Track operational performance of the API.

Metrics:

* Request volume
* Response latency
* Error rates
* Failed requests
* Service uptime

Alert Thresholds:

* Error rate > 2%
* Average response time > 1 second

## 5. Retraining Triggers

The model should be retrained when:

* Data drift exceeds acceptable thresholds
* Model performance degrades significantly
* New customer behavior patterns emerge
* Product offerings change substantially
* At least 6 months have passed since the previous training cycle

## Monitoring Frequency

* API monitoring: Continuous
* Data drift checks: Weekly
* Prediction quality review: Monthly
* Full model review: Quarterly
