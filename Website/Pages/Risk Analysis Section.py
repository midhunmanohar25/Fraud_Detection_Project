import streamlit as st
import pandas as pd
import pickle
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# Page Configuration
# ==========================================
st.set_page_config(
    page_title="Fraud Risk Dashboard",
    page_icon="📈",
    layout="wide"
)

# ==========================================
# Data Loading
# ==========================================
@st.cache_data # Caching prevents reloading data every time you click a filter
def load_data():
    # Load the processed dataframe
    df = pickle.load(open('models/df.pkl', 'rb'))
    # Ensure is_fraud is treated as a categorical string for better Plotly legends
    df['fraud_label'] = df['is_fraud'].map({1: 'Fraud', 0: 'Legitimate'})
    return df

df = load_data()

# ==========================================
# Dashboard Header
# ==========================================
st.title("📈 Fraud Risk Intelligence Dashboard")
st.markdown("Analyze historical transaction patterns, behavioral anomalies, and risk score distributions.")
st.markdown("---")

# ==========================================
# Top Level KPIs (Key Performance Indicators)
# ==========================================
total_txns = len(df)
total_fraud = df['is_fraud'].sum()
fraud_rate = total_fraud / total_txns
avg_amt = df['amount'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Transactions Analyzed", f"{total_txns:,}")
col2.metric("Detected Fraudulent Txns", f"{total_fraud:,}")
col3.metric("Overall Fraud Rate", f"{fraud_rate:.2%}")
col4.metric("Avg Transaction Value", f"${avg_amt:,.2f}")

st.markdown("---")

# ==========================================
# Row 1: Risk Distributions & Amounts
# ==========================================
col_risk, col_amt = st.columns(2)

with col_risk:
    st.subheader("Combined Risk Score Distribution")
    st.caption("How engineered risk scores separate fraud from legitimate transactions.")
    
    # Histogram showing the separation of classes based on your custom 'combined_risk'
    fig_risk = px.histogram(
        df, 
        x='combined_risk', 
        color='fraud_label',
        barmode='overlay',
        color_discrete_map={'Legitimate': '#2ecc71', 'Fraud': '#e74c3c'},
        opacity=0.75,
        labels={'combined_risk': 'Combined Risk Score'}
    )
    fig_risk.update_layout(yaxis_title="Count of Transactions", legend_title="")
    st.plotly_chart(fig_risk, use_container_width=True)

with col_amt:
    st.subheader("Transaction Amount Outliers")
    st.caption("Distribution of transaction amounts for Fraud vs Legitimate events.")
    
    # Box plot to show amount deviations
    fig_amt = px.box(
        df, 
        x='fraud_label', 
        y='amount', 
        color='fraud_label',
        color_discrete_map={'Legitimate': '#2ecc71', 'Fraud': '#e74c3c'}
    )
    fig_amt.update_layout(xaxis_title="", yaxis_title="Transaction Amount ($)", showlegend=False)
    st.plotly_chart(fig_amt, use_container_width=True)

# ==========================================
# Row 2: Categorical Risk Profiling
# ==========================================
st.markdown("---")
st.subheader("Merchant & Authentication Risk Profiling")

col_merch, col_auth = st.columns(2)

with col_merch:
    # Calculate fraud rate per merchant category
    merch_fraud = df.groupby('merchant_category')['is_fraud'].mean().reset_index()
    merch_fraud = merch_fraud.sort_values(by='is_fraud', ascending=True)
    
    fig_merch = px.bar(
        merch_fraud, 
        x='is_fraud', 
        y='merchant_category', 
        orientation='h',
        color='is_fraud',
        color_continuous_scale='Reds',
        labels={'is_fraud': 'Average Fraud Rate', 'merchant_category': 'Merchant Category'}
    )
    fig_merch.update_layout(coloraxis_showscale=False)
    fig_merch.update_xaxes(tickformat=".1%")
    st.plotly_chart(fig_merch, use_container_width=True)

with col_auth:
    # Compare authentication methods
    fig_auth = px.histogram(
        df, 
        x='authentication_method', 
        color='fraud_label',
        barmode='group',
        color_discrete_map={'Legitimate': '#3498db', 'Fraud': '#e74c3c'},
        labels={'authentication_method': 'Auth Method'}
    )
    fig_auth.update_layout(yaxis_title="Count", legend_title="")
    st.plotly_chart(fig_auth, use_container_width=True)

# ==========================================
# Row 3: Behavioral Anomalies (Telemetry)
# ==========================================
st.markdown("---")
st.subheader("Telemetry & Behavioral Red Flags")

col_ip, col_device = st.columns(2)

with col_ip:
    # Scatter plot of IP Risk vs Device Trust
    fig_scatter = px.scatter(
        df.sample(2000), # Sampled to 2000 points to keep the UI fast
        x='ip_address_risk_score', 
        y='device_trust_score', 
        color='fraud_label',
        color_discrete_map={'Legitimate': '#95a5a6', 'Fraud': '#e74c3c'},
        opacity=0.6,
        labels={'ip_address_risk_score': 'IP Risk Score', 'device_trust_score': 'Device Trust Score'}
    )
    fig_scatter.update_layout(legend_title="")
    st.plotly_chart(fig_scatter, use_container_width=True)

with col_device:
    # Heatmap of Device/Location change flags
    anomaly_df = df.groupby(['device_change_flag', 'location_change_flag'])['is_fraud'].mean().reset_index()
    anomaly_pivot = anomaly_df.pivot(index='device_change_flag', columns='location_change_flag', values='is_fraud')
    
    fig_heat = px.imshow(
        anomaly_pivot,
        text_auto=".1%",
        color_continuous_scale='Reds',
        labels=dict(x="Location Changed (1=Yes)", y="New Device (1=Yes)", color="Fraud Rate"),
        x=['No (0)', 'Yes (1)'],
        y=['No (0)', 'Yes (1)']
    )
    fig_heat.update_layout(coloraxis_showscale=False)
    st.plotly_chart(fig_heat, use_container_width=True)