import streamlit as st
import pandas as pd
from pymongo import MongoClient
import plotly.express as px
from datetime import datetime

MONGO_URI = "mongodb://localhost:27017"
client = MongoClient(MONGO_URI)
db = client["doctalk"]
collection = db["appointments"]

st.set_page_config(layout="wide")
st.title("DoctorTalk Analytics Dashboard")

@st.cache_data
def load_data():
    data = list(collection.find())
    df = pd.DataFrame(data)
    return df

df = load_data()

if df.empty:
    st.warning("No data found in MongoDB")
    st.stop()

df["bookedAt"] = pd.to_datetime(df["bookedAt"])
df["appointmentDate"] = pd.to_datetime(df["appointmentDate"])

df["wait_time_days"] = (df["appointmentDate"] - df["bookedAt"]).dt.days

total_appointments = len(df)
active_appointments = len(df[df["status"] == "booked"])
completed_appointments = len(df[df["status"] == "completed"])
cancelled_appointments = len(df[df["status"] == "cancelled"])

cancellation_rate = (cancelled_appointments / total_appointments) * 100
completion_rate = (completed_appointments / total_appointments) * 100
avg_wait_time = df["wait_time_days"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Appointments", total_appointments)
col2.metric("Active Appointments", active_appointments)
col3.metric("Cancellation Rate (%)", round(cancellation_rate, 2))
col4.metric("Avg Wait Time (Days)", round(avg_wait_time, 2))

st.divider()

region_counts = df["region"].value_counts().reset_index()
region_counts.columns = ["Region", "Count"]

fig_region = px.bar(
    region_counts,
    x="Region",
    y="Count",
    title="Appointments by Region"
)

st.plotly_chart(fig_region, use_container_width=True)

status_counts = df["status"].value_counts().reset_index()
status_counts.columns = ["Status", "Count"]

fig_status = px.pie(
    status_counts,
    values="Count",
    names="Status",
    title="Appointment Status Distribution"
)

st.plotly_chart(fig_status, use_container_width=True)

specialty_counts = df["specialty"].value_counts().reset_index()
specialty_counts.columns = ["Specialty", "Count"]

fig_specialty = px.bar(
    specialty_counts,
    x="Specialty",
    y="Count",
    title="Appointments by Specialty"
)

st.plotly_chart(fig_specialty, use_container_width=True)

df["month"] = df["bookedAt"].dt.to_period("M")
monthly_trend = df.groupby("month").size().reset_index(name="Count")
monthly_trend["month"] = monthly_trend["month"].astype(str)

fig_trend = px.line(
    monthly_trend,
    x="month",
    y="Count",
    markers=True,
    title="Monthly Booking Trend"
)

st.plotly_chart(fig_trend, use_container_width=True)

fig_wait = px.histogram(
    df,
    x="wait_time_days",
    nbins=20,
    title="Wait Time Distribution (Days)"
)

st.plotly_chart(fig_wait, use_container_width=True)

st.success("Dashboard Loaded Successfully 🚀")
