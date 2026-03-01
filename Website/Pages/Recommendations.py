import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Policy Recommendations",
    page_icon="🛡️",
    layout="wide"
)

# ==========================================
# Page Header
# ==========================================
st.title("🛡️ Risk Mitigation & Policy Recommendations")
st.markdown("""
Based on the machine learning model's historical analysis, this dashboard provides actionable 
**security policy recommendations** and **optimal threshold settings** to minimize financial loss 
while preserving a seamless customer experience.
""")
st.markdown("---")

# ==========================================
# Section 1: Optimal Threshold Recommendations
# ==========================================
st.subheader("⚙️ Recommended Model Thresholds")
st.write("Machine learning models output a probability from 0.0 to 1.0. Setting the right cutoff threshold is critical to balance fraud capture (Recall) and false alarms (Precision).")

col1, col2, col3 = st.columns(3)

with col1:
    st.success("### 🟢 Low Friction (Threshold: 0.70)")
    st.markdown("""
    * **Goal:** Maximize customer experience.
    * **Trade-off:** Misses some sophisticated fraud.
    * **Recommendation:** Use for low-value transactions (under $50) or highly trusted, returning customers.
    """)

with col2:
    st.warning("### 🟡 Balanced (Threshold: 0.50)")
    st.markdown("""
    * **Goal:** Optimal balance of F1-Score.
    * **Trade-off:** Moderate manual reviews required.
    * **Recommendation:** Use as the global default. Triggers step-up authentication (OTP) for suspicious behavior.
    """)

with col3:
    st.error("### 🔴 Maximum Security (Threshold: 0.30)")
    st.markdown("""
    * **Goal:** Catch absolutely all potential fraud (High Recall).
    * **Trade-off:** High false-positive rate; annoys legitimate users.
    * **Recommendation:** Use only for high-value transactions (over $10,000) or high-risk merchant categories (e.g., Crypto, Gaming).
    """)

st.markdown("---")

# ==========================================
# Section 2: Automated Rules Engine
# ==========================================
st.subheader("🛑 Recommended Hard Rules (Rules Engine)")
st.write("While the Gradient Boosting model handles complex patterns, we recommend implementing the following 'Hard Rules' at the gateway level to instantly block obvious threats.")

# Creating a simulated dataframe of recommended rules
rules_data = {
    "Rule ID": ["R-001", "R-002", "R-003", "R-004"],
    "Trigger Condition": [
        "IP Risk Score > 0.85 AND Device Trust < 0.2",
        "Transaction Amount > 3x Customer Average",
        "Location Changed AND New Device Flagged",
        "Merchant Fraud Rate > 15%"
    ],
    "Recommended Action": ["Hard Block", "Require OTP / PIN", "Require Manual Review", "Hold Funds (24h)"],
    "Estimated Impact": ["Prevents 12% of Account Takeovers", "Reduces high-value loss by 40%", "Stops 25% of unauthorized access", "Protects against risky merchants"]
}

rules_df = pd.DataFrame(rules_data)

# Displaying the rules beautifully in Streamlit
st.table(rules_df)

st.markdown("---")

# ==========================================
# Section 3: Merchant Category Advice
# ==========================================
st.subheader("🏬 Merchant-Specific Security Advice")

advice_col1, advice_col2 = st.columns([1, 2])

with advice_col1:
    # A simple pie chart simulating where fraud is concentrated
    fraud_concentration = pd.DataFrame({
        "Category": ["Electronics", "Gaming", "Travel", "Utilities", "Grocery", "Fashion"],
        "Fraud Focus": [35, 25, 20, 10, 5, 5]
    })
    
    fig = px.pie(fraud_concentration, values="Fraud Focus", names="Category", hole=0.4, title="Fraud Concentration by Category")
    st.plotly_chart(fig, use_container_width=True)

with advice_col2:
    st.write("### Target Categories")
    st.info("**Electronics & Gaming:** These categories suffer the highest fraud rates due to high resale value and instant delivery. **Recommendation:** Force multi-factor authentication (MFA) on all purchases over $200 in these categories.")
    
    st.write("### Safe Categories")
    st.success("**Utilities & Grocery:** These categories show historically low fraud rates. **Recommendation:** Implement a 'Fast-Track' checkout process with zero friction for returning customers.")