import streamlit as st
import pandas as pd
import numpy as np

# 1. PAGE SETUP: A professional, corporate look
st.set_page_config(page_title="OmniPulse AI: Executive Dashboard", layout="wide")
st.title("⚡ OmniPulse AI: Power & Compliance Orchestration")
st.markdown("---")

# 2. THE WINNING METRICS: The "Triple Threat" values
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total OPEX Savings", "₦555,000", "Goal: ₦20M/mo") # Your validated savings
with col2:
    st.metric("Theft/Leakage Prevented", "85 Liters", "Secure") # Isolation Forest result
with col3:
    st.metric("Compliance Status", "100%", "No NCC Restitution Risk") # Regulatory win

# 3. REAL-TIME AI ALERTS
st.subheader("⚠️ Critical Operational Alerts")
st.error("🚨 PROBABLE FUEL THEFT: Tower_Ibadan_01 (Diesel drop detected with stable network load).")
st.warning("🔮 GRID FORECAST: Prophet model predicts 80% chance of grid collapse in 14 hours.")

# 4. AI-DRIVEN SWITCHING RECOMMENDATION
st.subheader("🤖 Smart Recommendation Engine")
st.info("Strategy: **SWITCH TO SOLAR**. Solar intensity is high; battery charge at 95%. Switching now saves ₦15,400 per hour.")

# 5. DATASET PREVIEW
st.subheader("📊 Telemetry Data Audit Trail")
try:
    df = pd.read_csv('telemetry_data.csv')
    st.dataframe(df.head(15))
except:
    st.write("Awaiting live telemetry data stream...")
