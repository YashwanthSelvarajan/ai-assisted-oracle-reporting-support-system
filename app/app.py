import streamlit as st
import pandas as pd
from reporting_engine import calculate_kpis, department_summary, identify_priority_items
from summary_generator import generate_executive_summary, generate_recommendations

st.set_page_config(page_title="AI-Assisted Oracle Reporting Support System", layout="wide")

st.title("AI-Assisted Oracle Reporting & Business Decision Support System")
st.write(
    "This portfolio application demonstrates KPI reporting, SLA analysis, "
    "business decision support, and AI-assisted reporting summary logic."
)

uploaded_file = st.file_uploader("Upload a business reporting CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("data/sample_business_report.csv")

st.subheader("Business Reporting Dataset")
st.dataframe(df, use_container_width=True)

kpis = calculate_kpis(df)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total Requests", kpis["total_requests"])
col2.metric("Completed", kpis["completed_requests"])
col3.metric("SLA Breaches", kpis["breached_sla"])
col4.metric("Avg Cycle Time", f"{kpis['average_cycle_time_days']} days")
col5.metric("Estimated Savings", f"${kpis['total_estimated_savings']:,.0f}")

st.subheader("Department-Level Summary")
st.dataframe(department_summary(df), use_container_width=True)

st.subheader("High Priority / SLA Risk Items")
st.dataframe(identify_priority_items(df), use_container_width=True)

st.subheader("Executive Summary")
st.info(generate_executive_summary(kpis))

st.subheader("Recommended Actions")
for item in generate_recommendations(kpis):
    st.write(f"- {item}")
