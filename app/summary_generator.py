def generate_executive_summary(kpis):
    """Generate a stakeholder-friendly executive reporting summary."""
    return (
        f"The reporting dataset contains {kpis['total_requests']} total business requests. "
        f"{kpis['completed_requests']} requests have been completed, while "
        f"{kpis['breached_sla']} items have breached SLA expectations. "
        f"The average cycle time is {kpis['average_cycle_time_days']} days. "
        f"The estimated business savings opportunity is ${kpis['total_estimated_savings']:,.2f}. "
        "Leadership should prioritize breached SLA items and high-priority requests to improve operational efficiency."
    )

def generate_recommendations(kpis):
    """Create simple business recommendations based on KPI movement."""
    recommendations = []

    if kpis["breached_sla"] > 0:
        recommendations.append("Review SLA-breached requests and identify approval or processing delays.")

    if kpis["average_cycle_time_days"] > 5:
        recommendations.append("Analyze process bottlenecks and automate recurring manual reporting steps.")

    if kpis["total_estimated_savings"] > 10000:
        recommendations.append("Prioritize automation initiatives with the highest estimated savings impact.")

    if not recommendations:
        recommendations.append("Current reporting performance appears stable. Continue monitoring KPI trends.")

    return recommendations
