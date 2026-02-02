-- =====================================
-- STEP 04: Business Analytics Layer
-- Source : transactions_raw
-- Target : transactions_analytics
-- =====================================

DROP TABLE IF EXISTS transactions_analytics;

CREATE TABLE transactions_analytics AS
SELECT
    -- Customer & Account
    customer_id,
    gender,
    age,
    account_type,

    -- Geography
    state,
    city,

    -- Transaction Identity
    transaction_id,
    transaction_date,
    transaction_time,

    -- Time Derivations
    DATE_TRUNC('month', transaction_date) AS transaction_month,
    EXTRACT(HOUR FROM transaction_time::time) AS transaction_hour,

    -- Financials
    transaction_amount,
    account_balance,

    -- Categoricals
    merchant_category,
    transaction_type,
    device_type,

    -- Fraud Label
    is_fraud

FROM transactions_raw;
