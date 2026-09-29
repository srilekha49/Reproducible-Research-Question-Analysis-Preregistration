# PREREGISTRATION PROTOCOL: STUDY PROTOCOL-2026-DEMAND-01
**Timestamp:** 2026-09-29T10:50:00Z  
**Status:** LOCKED PRE-ANALYSIS PLAN (DATA-BLIND)

---

## Research Question
Does the activation of a marketing event (`marketing_event = 1`) significantly increase daily product demand (`demand`) compared to standard non-event days, and how does the presence of a holiday (`holiday = 1`) moderate this effect?

---

## Hypotheses

### Primary Outcome: Daily Demand Volume ($Y$)
* **Null Hypothesis ($H_{0,1}$):** Mean daily product demand on marketing event days is less than or equal to mean daily demand on standard non-event days.
  $$\mu_{\text{demand, marketing=1}} \le \mu_{\text{demand, marketing=0}}$$
* **Alternative Hypothesis ($H_{1,1}$):** Mean daily product demand on marketing event days is significantly higher than on standard non-event days.
  $$\mu_{\text{demand, marketing=1}} > \mu_{\text{demand, marketing=0}}$$

### Moderating Effect: Holiday Interaction
* **Null Hypothesis ($H_{0,2}$):** There is no significant interaction effect between marketing events and holidays on daily demand.
* **Alternative Hypothesis ($H_{1,2}$):** The combination of a marketing event and holiday produces a non-additive shift in daily product demand.

---

## Population, Sample, and Exclusions
* **Target Population:** Daily retail transaction records across mid-year commercial operating windows.
* **Unit of Analysis:** Individual operating day.
* **Inclusion Rules:**
  1. Complete 24-hour daily demand logging.
  2. Dates falling strictly within the June 2026 observation window.
* **Exclusion Rules:**
  1. Days with reported system outage or catalog unavailability.
  2. Partial reporting days ($<24$ hours of record).
* **Stopping Rule:** Fixed observational sample of 30 consecutive calendar days ($N=30$). No dynamic sample extension or post-hoc sampling.

---

## Variables and Measures

| Variable Name | Role | Type | Definition / Transformation |
| :--- | :--- | :--- | :--- |
| **`demand`** | Primary Outcome | Continuous | Daily unit demand count. Log transformation ($\ln(\text{demand})$) evaluated if right-skewed. |
| **`marketing_event`** | Primary Predictor | Binary | 1 = Active marketing promotion, 0 = Baseline |
| **`holiday`** | Secondary Predictor / Moderator | Binary | 1 = Official holiday, 0 = Non-holiday |
| **`day_of_week`** | Control Variable | Categorical | Derived from `date` (Monday–Sunday) to control for weekly seasonality. |

* **Missing Data Protocol:** Complete case analysis. (If missing values occur, listwise deletion if $<5\%$, or forward-fill for time-series continuity).

---

## Analysis Plan
* **Primary Hypothesis Test:** Two-sample independent $t$-test and Mann-Whitney $U$ test comparing demand across `marketing_event` groups.
* **Distributional Normality Tests:** Shapiro-Wilk test and Kolmogorov-Smirnov test evaluated at $\alpha = 0.05$.
* **ANOVA Framework:**
  * **One-Way ANOVA:** Demand across combined event categories (`Baseline`, `Marketing Only`, `Holiday Only`).
  * **Two-Way ANOVA:** Factorial model examining main effects of `marketing_event`, `holiday`, and their interaction term (`marketing_event` $\times$ `holiday`).
* **Post-Hoc Analysis:** Tukey’s Honestly Significant Difference (HSD) test across treatment group pairs.
* **Assumptions & Alpha Level:** Significance threshold $\alpha = 0.05$. Levene’s test for equality of variances.
* **Effect Sizes:** Cohen's $d$ for two-sample differences, Partial Eta-Squared ($\eta_p^2$) for ANOVA models.
* **Robustness Checks:** Ordinary Least Squares (OLS) regression controlling for day-of-week seasonality and autocorrelation-robust standard errors (HAC / Newey-West).

---

## Deviations Log

| Timestamp (UTC) | Protocol Section | Planned Protocol | Executed Deviation | Justification / Reason |
| :--- | :--- | :--- | :--- | :--- |
| *2026-09-29 10:50* | Protocol Lock | Initial locked plan | None | Protocol finalized prior to inferential testing. |