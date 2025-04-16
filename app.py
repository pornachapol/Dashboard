
import streamlit as st
import pandas as pd
import altair as alt

# ข้อมูลหลัก
data = pd.DataFrame([
    {"year": "2025", "revenue": 2.4, "cost": 6.5, "profit": -4.1},
    {"year": "2026", "revenue": 12, "cost": 4, "profit": 8},
    {"year": "2027", "revenue": 36, "cost": 5, "profit": 31}
])

# คำนวณ ROI รายปี และสะสม
data["roi"] = (data["profit"] / data["cost"] * 100).round(1)
data["cumulative_profit"] = data["profit"].cumsum()
data["cumulative_cost"] = data["cost"].cumsum()
data["cumulative_roi"] = (data["cumulative_profit"] / data["cumulative_cost"] * 100).round(1)

# คำนวณ Break-even Point
def calculate_break_even_month(data):
    cum_profit = data["cumulative_profit"].tolist()
    for i in range(1, len(cum_profit)):
        if cum_profit[i] >= 0:
            prev = cum_profit[i-1]
            curr = cum_profit[i]
            ratio = abs(prev) / (curr - prev)
            return int((i-1)*12 + ratio*12)
    return "Not within 3 years"

break_even_months = calculate_break_even_month(data)
break_even_years = round(break_even_months/12, 1) if isinstance(break_even_months, (int, float)) else break_even_months

# UI Start
st.title("📊 Financial ROI Dashboard (2025–2027)")

col1, col2, col3 = st.columns(3)
col1.metric("Initial Investment", "5.5 MB")
col2.metric("Break-even Point", f"{break_even_months} months", f"≈ {break_even_years} yrs")
col3.metric("3-Year ROI", f"{data['cumulative_roi'].iloc[-1]}%")

st.subheader("📈 Revenue, Cost & Profit (MB)")
line = alt.Chart(data).transform_fold(
    ["revenue", "cost", "profit"],
    as_=["Metric", "Value"]
).mark_line(point=True).encode(
    x="year",
    y="Value:Q",
    color="Metric:N"
).properties(height=300)
st.altair_chart(line, use_container_width=True)

st.subheader("💹 Annual & Cumulative ROI (%)")
roi_chart = alt.Chart(data).transform_fold(
    ["roi", "cumulative_roi"],
    as_=["Metric", "Value"]
).mark_line(point=True).encode(
    x="year",
    y="Value:Q",
    color="Metric:N"
).properties(height=300)
st.altair_chart(roi_chart, use_container_width=True)

st.subheader("📊 Cumulative Profit for Break-even Analysis")
cum_profit_chart = alt.Chart(data).mark_line(point=True).encode(
    x="year",
    y="cumulative_profit",
    tooltip=["year", "cumulative_profit"]
).properties(height=300)
st.altair_chart(cum_profit_chart, use_container_width=True)

st.caption("Dashboard by ChatGPT | Based on 5.5MB Dev Cost Investment")
