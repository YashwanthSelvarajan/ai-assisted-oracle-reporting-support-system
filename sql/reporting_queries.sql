-- ==========================================================
-- SQL reporting examples for AI-Assisted Oracle Reporting System
-- These queries can be adapted for Oracle SQL dashboards.
-- ==========================================================

-- KPI summary by department
SELECT
    department,
    COUNT(*) AS total_requests,
    ROUND(AVG(cycle_time_days), 2) AS avg_cycle_time,
    SUM(estimated_savings) AS total_estimated_savings
FROM business_reporting_data
GROUP BY department;

-- SLA breach report
SELECT
    request_id,
    department,
    request_type,
    priority,
    status,
    cycle_time_days,
    sla_status
FROM business_reporting_data
WHERE sla_status = 'BREACHED'
ORDER BY cycle_time_days DESC;

-- High-priority operational risk report
SELECT
    request_id,
    department,
    request_type,
    priority,
    status,
    estimated_savings
FROM business_reporting_data
WHERE priority IN ('HIGH', 'CRITICAL')
ORDER BY estimated_savings DESC;
