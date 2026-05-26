import pandas as pd

def load_report_data(uploaded_file=None, default_path="data/sample_business_report.csv"):
    """Load business reporting data from an uploaded CSV file or default sample file."""
    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)
    return pd.read_csv(default_path)

def calculate_kpis(df):
    """Calculate KPI metrics used for reporting dashboards."""
    total_requests = len(df)
    completed_requests = len(df[df["status"] == "COMPLETED"])
    breached_sla = len(df[df["sla_status"] == "BREACHED"])
    avg_cycle_time = round(df["cycle_time_days"].mean(), 2)
    total_estimated_savings = round(df["estimated_savings"].sum(), 2)

    return {
        "total_requests": total_requests,
        "completed_requests": completed_requests,
        "breached_sla": breached_sla,
        "average_cycle_time_days": avg_cycle_time,
        "total_estimated_savings": total_estimated_savings
    }

def department_summary(df):
    """Create department-level reporting summary."""
    return (
        df.groupby("department")
        .agg(
            total_requests=("request_id", "count"),
            avg_cycle_time=("cycle_time_days", "mean"),
            total_savings=("estimated_savings", "sum")
        )
        .reset_index()
        .round(2)
    )

def identify_priority_items(df):
    """Identify high-risk items requiring stakeholder attention."""
    return df[
        (df["priority"].isin(["HIGH", "CRITICAL"])) |
        (df["sla_status"] == "BREACHED")
    ].sort_values(by=["cycle_time_days"], ascending=False)
