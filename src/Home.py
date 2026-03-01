import streamlit as st

st.set_page_config(
    page_title="Digital Payment Fraud Detection System",
    page_icon="🛡️",
    layout="wide"
)

# ===============================
# Title
# ===============================
st.markdown("# 🛡️ Digital Payment Fraud Detection System")

st.markdown(
    """
    Welcome to the **Digital Payment Fraud Detection Platform**, an intelligent machine learning system 
    designed to identify and prevent fraudulent online transactions in real-time.

    This platform leverages advanced **behavioral analytics**, **risk scoring**, and **machine learning models**
    to detect suspicious activities across digital payments such as UPI, cards, and online transactions.
    """
)

st.info("👈 Use the sidebar to navigate between Fraud Prediction and Risk Analysis modules.")

st.divider()

# ===============================
# Fraud Prediction Section
# ===============================
st.markdown(
    """
    ## 🔎 Real-Time Fraud Prediction

    The **Fraud Prediction Module** allows users to simulate a digital transaction 
    and instantly determine whether it is **legitimate or potentially fraudulent**.

    The model evaluates multiple behavioral and risk-based indicators such as:

    - IP address risk score  
    - Merchant historical fraud rate  
    - Device change & location change flags  
    - OTP success rate and authentication behavior  
    - Transaction amount deviation from customer history  
    - Transaction velocity (recent activity patterns)  
    - International transaction flag  
    - Time-based features (hour of day, weekend indicator)

    Based on these signals, the system outputs:

    ✅ Fraud probability score  
    🚨 Fraud / Not Fraud classification  
    📊 Risk interpretation
    """
)

st.info("⚡ Enter transaction details to evaluate fraud probability instantly.")

st.divider()

# ===============================
# Risk Analysis Section
# ===============================
st.markdown(
    """
    ## 📊 Fraud Risk Intelligence Dashboard

    The **Risk Analysis Module** provides insights into transaction behavior and fraud trends through:

    - Feature importance analysis  
    - Risk score distribution visualization  
    - Fraud vs Non-Fraud comparison plots  
    - Time-based fraud pattern analysis  
    - Merchant & customer risk profiling  

    These analytics help businesses understand fraud patterns,
    detect anomalies, and improve fraud prevention strategies.
    """
)

st.info("📈 Explore fraud trends and behavioral risk patterns.")

st.divider()

# ===============================
# Model Information Section
# ===============================
st.markdown(
    """
    ## 🤖 Machine Learning Model

    This system is built using:

    - Advanced feature engineering with historical behavioral tracking  
    - Risk-based anomaly indicators  
    - Imbalance-aware classification techniques  
    - Threshold tuning for optimized recall and precision  
    - Production-style pipeline design  

    The model is optimized to maximize **fraud detection recall** 
    while maintaining acceptable precision to reduce false alarms.
    """
)

st.divider()

st.markdown(
    """
    ✨ Whether you are a **financial institution**, **fintech company**, or **risk analyst**,  
    this platform delivers a robust, data-driven approach to fraud prevention.
    """
)

# ===============================
# Navigation Button to Predict Page
# ===============================

st.markdown("### 🚀 Ready to Test a Transaction?")

# Primary Call-to-Action Button
if st.button("Go to Fraud Prediction Page", type="primary", use_container_width=True):
    st.switch_page("Pages/Fraud Risk Engine.py")  # Ensure your folder name matches exactly
        
st.caption("👈 Or select a module from the sidebar menu to get started.")

#-----------------------------------------------------------------------------------------------------------------------------------
# import streamlit as st

# st.set_page_config(
#     page_title="Digital Payment Fraud Detection System",
#     page_icon="🛡️",
#     layout="wide"
# )

# # ===============================
# # Hero Section (Centered & Clean)
# # ===============================
# st.markdown("<h1 style='text-align: center;'>🛡️ Digital Payment Fraud Detection System</h1>", unsafe_allow_html=True)
# st.markdown("<h4 style='text-align: center; color: gray;'>An intelligent machine learning platform designed to identify and prevent fraudulent online transactions in real-time.</h4>", unsafe_allow_html=True)

# st.write("")
# st.write("")

# # ===============================
# # Feature Cards (3-Column Layout)
# # ===============================
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.info("### 🔎 Real-Time Prediction\n"
#             "Simulate a digital transaction and instantly determine whether it is legitimate or potentially fraudulent.\n\n"
#             "**Outputs:**\n"
#             "* ✅ Fraud probability score\n"
#             "* 🚨 Fraud / Not Fraud classification\n"
#             "* 📊 Risk interpretation"
#             )

# with col2:
#     st.warning("### 📊 Risk Intelligence\n"
#             "Gain insights into transaction behavior and fraud trends through our analytics dashboard.\n\n"
#             "**Features:**\n"
#             "* Feature importance analysis\n"
#             "* Risk score distribution\n"
#             "* Time-based fraud patterns"
#             )

# with col3:
#     st.success("### 🤖 Machine Learning Engine\n"
#             "Built with a robust, production-style pipeline optimized to maximize fraud detection recall.\n\n"
#             "**Powered By:**\n"
#             "* Advanced behavioral engineering\n"
#             "* SMOTE for imbalanced data\n"
#             "* Gradient Boosting Classifier"
#             )

# st.write("")
# st.markdown("---")

# # ===============================
# # Deep Dive & Call to Action
# # ===============================
# col_text, col_cta = st.columns([2, 1], gap="large")

# with col_text:
#     st.subheader("Key Behavioral Indicators Analyzed")
#     st.markdown(
#         """
#         The model evaluates multiple behavioral and risk-based signals to catch anomalies:
#         - **Trust & Telemetry:** IP address risk score, device trust score, and device/location change flags.
#         - **Historical Context:** Merchant historical fraud rate and customer past fraud counts.
#         - **Authentication:** OTP success rate and PIN verification behavior.
#         - **Velocity & Deviation:** Transaction amount deviation from customer history and 24-hour volume patterns.
#         - **Contextual Flags:** International transaction flags, weekend indicators, and time of day.
#         """
#     )

# with col_cta:
#     st.write("")
#     st.write("")
#     st.markdown("### 🚀 Ready to Test a Transaction?")
#     st.write("Whether you are a financial institution, fintech company, or risk analyst, test the platform's robust, data-driven approach.")
    
#     # Primary Call-to-Action Button
#     if st.button("Go to Fraud Prediction Page", type="primary", use_container_width=True):
#         st.switch_page("Pages/Classify.py")  # Ensure your folder name matches exactly
        
#     st.caption("👈 Or select a module from the sidebar menu to get started.")