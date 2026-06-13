# Monitoring Plan

## Purpose

The D2C Customer Churn Prediction API is designed to support customer retention teams by identifying customers who are likely to churn within the next 60 days.

To ensure the system remains accurate, reliable, and aligned with business objectives, continuous monitoring must be performed across data quality, model behavior, prediction outputs, business outcomes, and operational performance.

This monitoring framework defines what should be measured, acceptable thresholds, alerting criteria, ownership responsibilities, and retraining triggers.

---

# 1. Data Drift Monitoring

## Objective

Ensure incoming customer data remains consistent with the data used during model training.

Changes in customer purchasing behavior, engagement patterns, marketing response, or support interactions may reduce model effectiveness and require investigation or retraining.

## Critical Features to Monitor

### Customer Behavior

* recency_days
* frequency_180d
* monetary_180d
* return_rate_180d

### Customer Engagement

* sessions_30d
* product_views_30d
* cart_adds_30d
* email_opens_30d
* campaign_clicks_30d

### Customer Support

* ticket_count_90d
* negative_ticket_rate_90d
* avg_resolution_hours_90d

## Monitoring Metrics

* Population Stability Index (PSI)
* Feature distribution comparison
* Mean and median shifts
* Missing value rates
* Outlier frequency
* Category frequency changes
* New categorical values detected

## Alert Thresholds

| Metric                | Alert Level            |
| --------------------- | ---------------------- |
| PSI > 0.10            | Investigation Required |
| PSI > 0.25            | Significant Drift      |
| Missing Values > 5%   | Data Quality Review    |
| New Category Detected | Validation Required    |

## Monitoring Frequency

Weekly

---

# 2. Prediction Distribution Monitoring

## Objective

Monitor the stability of model outputs over time.

Significant shifts in churn predictions may indicate data drift, customer behavior changes, model degradation, or business environment changes.

## Metrics

* Average churn probability
* Median churn probability
* Churn probability distribution
* High-risk customer percentage
* Medium-risk customer percentage
* Low-risk customer percentage

## Risk Definitions

| Risk Level | Probability Range |
| ---------- | ----------------- |
| Low        | < 0.45            |
| Medium     | 0.45 – 0.74       |
| High       | ≥ 0.75            |

## Alert Thresholds

* Prediction distribution shift greater than 20%
* High-risk customer segment growth greater than 15%
* Average churn probability increases by more than 10%
* Sudden drop in medium-risk population

## Monitoring Frequency

Weekly

---

# 3. Model Performance Monitoring

## Objective

Validate that prediction quality remains acceptable once actual churn outcomes become available.

## Core Performance Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* PR-AUC

## Performance Degradation Triggers

| Metric                  | Retraining Review |
| ----------------------- | ----------------- |
| Precision drops by >10% | Yes               |
| Recall drops by >10%    | Yes               |
| F1 Score drops by >10%  | Yes               |
| ROC-AUC < 0.80          | Yes               |

## Monitoring Frequency

Monthly

---

# 4. Model Confidence & Calibration Monitoring

## Objective

Ensure predicted probabilities remain meaningful and calibrated.

A customer predicted with 80% churn probability should churn approximately 80% of the time across similar customers.

## Metrics

* Calibration Curve
* Brier Score
* Probability Reliability Analysis
* Confidence Distribution
* Probability Bucket Analysis

## Alert Thresholds

* Significant calibration drift
* Probability concentration in a narrow range
* Confidence distribution changes greater than 15%

## Monitoring Frequency

Monthly

---

# 5. Business Outcome Monitoring

## Objective

Measure whether the churn prediction system delivers measurable business value.

## Retention Effectiveness

* Retention campaign conversion rate
* Customer re-engagement rate
* High-risk customer save rate
* Offer acceptance rate

## Revenue Impact

* Revenue retained
* Customer lifetime value retained
* Incremental revenue recovered
* Campaign ROI

## Churn Outcomes

* Actual churn rate
* Churn reduction percentage
* Segment-level churn trends

## Success Indicators

* Reduction in overall churn rate
* Increased retention campaign effectiveness
* Positive campaign ROI
* Improved customer engagement metrics

## Monitoring Frequency

Monthly

---

# 6. API Reliability Monitoring

## Objective

Ensure the prediction service remains available, responsive, and reliable.

## Availability Metrics

* Uptime percentage
* Service availability
* Health-check success rate

## Performance Metrics

* Average response time
* P95 latency
* P99 latency

## Reliability Metrics

* Error rate
* Failed requests
* Timeout rate
* Server exceptions

## Alert Thresholds

| Metric                     | Alert Level            |
| -------------------------- | ---------------------- |
| Error Rate > 2%            | Investigation Required |
| Error Rate > 5%            | Critical               |
| Average Latency > 1 second | Investigation Required |
| Uptime < 99%               | Critical               |

## Monitoring Frequency

Continuous

---

# 7. API Usage Monitoring

## Objective

Track system adoption, request patterns, and API utilization.

## Metrics

### Traffic

* Request volume
* Requests per minute (RPM)
* Requests per hour
* Daily active users

### Endpoint Usage

* /predict request volume
* /batch_predict request volume
* /health request volume

### Validation Monitoring

* 422 validation errors
* Invalid payload frequency
* Failed batch submissions

### Batch Usage

* Average batch size
* Largest batch size
* Batch prediction frequency

## Alert Thresholds

| Metric                     | Alert Level            |
| -------------------------- | ---------------------- |
| Validation Errors > 10%    | Investigation Required |
| Sudden Traffic Spike > 50% | Review Required        |
| Batch Failures > 5%        | Investigation Required |

## Monitoring Frequency

Continuous

---

# 8. Retraining Strategy

## Objective

Maintain model effectiveness as customer behavior evolves.

## Data-Based Triggers

* PSI exceeds 0.25
* Significant feature distribution shifts
* New customer behavior patterns emerge

## Performance-Based Triggers

* Precision declines by more than 10%
* Recall declines by more than 10%
* F1 Score declines by more than 10%
* ROC-AUC falls below target levels

## Business-Based Triggers

* Retention campaign effectiveness declines
* Customer acquisition strategy changes
* Product portfolio changes significantly
* Customer lifecycle behavior changes

## Time-Based Trigger

Mandatory retraining every 6 months.

---

# 9. Monitoring Ownership

| Area                  | Responsible Team       |
| --------------------- | ---------------------- |
| Data Quality          | Data Engineering       |
| Data Drift            | Data Science           |
| Prediction Monitoring | Data Science           |
| Model Calibration     | Data Science           |
| API Reliability       | Engineering            |
| API Usage Monitoring  | Engineering            |
| Business Outcomes     | Marketing & Retention  |
| Retraining Decisions  | Data Science & Product |

---

# Monitoring Schedule Summary

| Activity                       | Frequency      |
| ------------------------------ | -------------- |
| API Health Monitoring          | Continuous     |
| API Usage Monitoring           | Continuous     |
| Data Quality Checks            | Weekly         |
| Data Drift Analysis            | Weekly         |
| Prediction Distribution Review | Weekly         |
| Model Calibration Review       | Monthly        |
| Model Performance Review       | Monthly        |
| Business KPI Review            | Monthly        |
| Full Model Audit               | Quarterly      |
| Scheduled Retraining           | Every 6 Months |

---

# Conclusion

The monitoring framework ensures that the D2C Customer Churn Prediction API remains reliable, interpretable, and business-aligned throughout its lifecycle.

By continuously monitoring data quality, model performance, calibration, prediction distributions, API reliability, business outcomes, and system usage, the organization can proactively detect issues, maintain model effectiveness, and maximize retention value while ensuring responsible deployment practices.
