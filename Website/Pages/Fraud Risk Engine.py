# import streamlit as st
# import pandas as pd
# import numpy as np
# import pickle

# st.set_page_config(page_title="Predict")

# df = pickle.load(open('models\df.pkl', 'rb'))

# pipeline = pickle.load(open('models\pipeline.pkl', 'rb'))

# # # -----------------------------------------------------Initialization-------------------------------------------------------------

# df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# merchant_fraud_dict = df.groupby('merchant_category')['merchant_fraud_rate'].mean().to_dict()
# merchant_hist_fraud_dict = df.groupby('merchant_category')['merchant_historical_fraud_rate'].mean().to_dict()


# #-----------------------------------------------------User Inputs-----------------------------------------------------------------
# st.header("Enter Your Inputs")

# # Customer ID
# customer_id = st.number_input("Customer ID")

# customer_id = int(customer_id)


# # Day and Months
# import datetime
# transaction_date = st.date_input("Transaction Date", datetime.date.today())
# month = transaction_date.month
# day = transaction_date.day


# # Payment Method
# payment_method = st.selectbox('Payment Method',df['payment_method'].unique().tolist())


# # Merchant Category
# merchant_category = st.selectbox('Merchant Category', df['merchant_category'].unique().tolist())


# # Authentication Method
# authentication_method = st.selectbox('Authentication Method', df['authentication_method'].unique().tolist())


# # Transaction Amount
# amount = st.number_input("Transaction Amount", min_value=0.0)


# st.markdown("---")

# st.header("2. Background Telemetry (Simulated for Testing)")
# st.write("In a real environment, these scores are fetched silently via third-party APIs.")

# # IP Risk Score
# ip_address_risk_score = st.slider("IP Risk Score", 0.0, 1.0)


# # Device Trust Score
# device_trust_score = st.slider("Device Trust Score", 0.0, 1.0)


# # Device Change Flag
# device_change = st.radio("Is this a new device?", ["No", "Yes"])
# if device_change == "Yes":
#     device_change_flag = 1
# else:
#     device_change_flag = 0

# # Location Change Flag
# location_change = st.radio("Is location changed?", ["No", "Yes"])
# if location_change == "Yes":
#     location_change_flag = 1
# else:
#     location_change_flag = 0

# # International Transaction Flag
# is_international_input = st.radio("Is this an international transaction?", ["No", "Yes"])
# if is_international_input == "Yes":
#     is_international = 1
# else:
#     is_international = 0

# #-------------------------------------------------------Calculated Inputs-----------------------------------------------------------
    
# # Avrage Amount Last 24h
# avg_amount_last_24h = df.loc[df['customer_id'] == customer_id, 'avg_amount_last_24h'].max()



# # Customer Transaction Count
# cust_txn_count = int(df.loc[df['customer_id'] == customer_id, 'customer_id'].count())



# # Customer Fraud Count
# cust_fraud_count = df.loc[df['customer_id'] == customer_id, 'is_fraud'].sum()
# if pd.notna(cust_fraud_count):
#     cust_fraud_count = int(cust_fraud_count)
# else:
#     cust_fraud_count = 0



# # Customer Fraud rate
# cust_fraud_rate = df.loc[df['customer_id'] == customer_id, 'is_fraud'].mean()



# # Customer Average Amount
# cust_avg_amt = df.loc[df['customer_id'] == customer_id, 'amount'].mean()


# # Device Count
# device_count = df.loc[df['customer_id'] == customer_id, 'device_count'].max()
# if pd.notna(device_count):
#     device_count = int(device_count)
# else:
#     device_count = 0



# # For Merchant Fraud Rate


# # Merchant Historical Fraud Rate
# merchant_historical_fraud_rate = merchant_hist_fraud_dict[merchant_category]

# # Merchant Fruad Rate
# merchant_fraud_rate = merchant_fraud_dict[merchant_category]




# # For Combined Risk
# otp_success = df.loc[df['customer_id'] == customer_id, 'otp_success_rate_customer'].mean()

# # Fallback to a default value (e.g., 0.5) if the customer is brand new
# if pd.isna(otp_success):
#     otp_success = 0.5 

# otp_risk = 1 - otp_success
# combined_risk = (0.3 * merchant_fraud_rate) + (0.3 * cust_fraud_rate) + (0.2 * otp_risk) + (0.2 * is_international)



# #-------------------------------------------------------------------------------------------------------------------------------------

# if st.button("Run Risk Assessment"):

#     # 2. Prepare Feature Vector (Must match training column order)
#     input_data = pd.DataFrame({
#         'payment_method' : [payment_method],
#         'merchant_category' : [merchant_category],
#         'authentication_method' : [authentication_method],
#         'amount': [amount],
#         'ip_address_risk_score': [ip_address_risk_score],
#         'device_trust_score': [device_trust_score],
#         'avg_amount_last_24h': [avg_amount_last_24h],
#         'device_change_flag': [device_change_flag],
#         'location_change_flag': [location_change_flag],
#         'merchant_historical_fraud_rate': [merchant_historical_fraud_rate],
#         'cust_txn_count': [cust_txn_count],
#         'cust_fraud_count': [cust_fraud_count],
#         'cust_fraud_rate': [cust_fraud_rate],
#         'cust_avg_amt': [cust_avg_amt],
#         'device_count': [device_count],
#         'merchant_fraud_rate': [merchant_fraud_rate],
#         'combined_risk': [combined_risk],
#         'month': [month],
#         'day': [day],
#         # Add all other features your model was trained on...
#     })

#     # 3. Prediction
#     prediction = pipeline.predict(input_data)[0]
#     probability = pipeline.predict_proba(input_data)[0][1]

#     # 4. Results Display
#     st.subheader("Risk Analysis Result")
        
#     if probability > 0.7:
#         st.error(f"⚠️ HIGH RISK: Fraud Probability {probability:.2%}")
#         st.write("**Recommended Action:** Hard Block & Device Lock")
#     elif probability > 0.4:
#         st.warning(f"🟡 MEDIUM RISK: Fraud Probability {probability:.2%}")
#         st.write("**Recommended Action:** Trigger Mandatory OTP / Manual Review")
#     else:
#         st.success(f"✅ LOW RISK: Fraud Probability {probability:.2%}")
#         st.write("**Recommended Action:** Approve Transaction")

#     # Visualization of Feature Importance or Risk
#     st.progress(probability)
# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


import streamlit as st
import pandas as pd
import numpy as np
import pickle
import datetime

# 1. Page Configuration (Added icon and layout style)
st.set_page_config(page_title="Fraud Risk Engine", page_icon="🛡️", layout="centered")

# Load Models
df = pickle.load(open('models\df.pkl', 'rb'))
pipeline = pickle.load(open('models\pipeline.pkl', 'rb'))

# -----------------------------------------------------Initialization-------------------------------------------------------------
df['transaction_date'] = pd.to_datetime(df['transaction_date'])

merchant_fraud_dict = df.groupby('merchant_category')['merchant_fraud_rate'].mean().to_dict()
merchant_hist_fraud_dict = df.groupby('merchant_category')['merchant_historical_fraud_rate'].mean().to_dict()

# -----------------------------------------------------Header-----------------------------------------------------------------
st.title("🛡️ Fraud Risk Assessment Engine")
st.caption("Enter transaction details below to evaluate the probability of fraudulent activity using the Gradient Boosting model.")
st.markdown("---")

# -----------------------------------------------------User Inputs-----------------------------------------------------------------
st.subheader("👤 1. Transaction Details")

# Using columns to put inputs side-by-side for a cleaner look
col1, col2 = st.columns(2)

with col1:
    customer_id = st.number_input("Customer ID", min_value=1, value=1001)
    customer_id = int(customer_id)
    amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=150.00)
    transaction_date = st.date_input("Transaction Date", datetime.date.today())

with col2:
    merchant_category = st.selectbox('Merchant Category', df['merchant_category'].unique().tolist())
    payment_method = st.selectbox('Payment Method', df['payment_method'].unique().tolist())
    authentication_method = st.selectbox('Authentication Method', df['authentication_method'].unique().tolist())

month = transaction_date.month
day = transaction_date.day

st.markdown("---")

# -----------------------------------------------------Telemetry Inputs-------------------------------------------------------------
st.subheader("⚙️ 2. Background Telemetry")
st.info("💡 **Simulated for Testing:** In a production environment, these metrics are fetched silently via third-party APIs and device fingerprinting.")

col3, col4 = st.columns(2)

with col3:
    ip_address_risk_score = st.slider("IP Risk Score", 0.0, 1.0, 0.2)
    device_trust_score = st.slider("Device Trust Score", 0.0, 1.0, 0.8)

with col4:
    # horizontal=True makes radio buttons look like clean pill toggles
    device_change = st.radio("Is this a new device?", ["No", "Yes"], horizontal=True)
    device_change_flag = 1 if device_change == "Yes" else 0

    location_change = st.radio("Is location changed?", ["No", "Yes"], horizontal=True)
    location_change_flag = 1 if location_change == "Yes" else 0

    is_international_input = st.radio("Is this an international transaction?", ["No", "Yes"], horizontal=True)
    is_international = 1 if is_international_input == "Yes" else 0

st.markdown("---")

#-------------------------------------------------------Calculated Inputs-----------------------------------------------------------
# Average Amount Last 24h
avg_amount_last_24h = df.loc[df['customer_id'] == customer_id, 'avg_amount_last_24h'].max()
if pd.isna(avg_amount_last_24h): avg_amount_last_24h = 0.0

# Customer Transaction Count
cust_txn_count = int(df.loc[df['customer_id'] == customer_id, 'customer_id'].count())

# Customer Fraud Count
cust_fraud_count = df.loc[df['customer_id'] == customer_id, 'is_fraud'].sum()
cust_fraud_count = int(cust_fraud_count) if pd.notna(cust_fraud_count) else 0

# Customer Fraud rate
cust_fraud_rate = df.loc[df['customer_id'] == customer_id, 'is_fraud'].mean()
cust_fraud_rate = float(cust_fraud_rate) if pd.notna(cust_fraud_rate) else 0.0

# Customer Average Amount
cust_avg_amt = df.loc[df['customer_id'] == customer_id, 'amount'].mean()
if pd.isna(cust_avg_amt): cust_avg_amt = 0.0

# Device Count
device_count = df.loc[df['customer_id'] == customer_id, 'device_count'].max()
device_count = int(device_count) if pd.notna(device_count) else 0

# Merchant Historical Fraud Rate
merchant_historical_fraud_rate = merchant_hist_fraud_dict.get(merchant_category, 0.0)

# Merchant Fraud Rate
merchant_fraud_rate = merchant_fraud_dict.get(merchant_category, 0.0)

# For Combined Risk
otp_success = df.loc[df['customer_id'] == customer_id, 'otp_success_rate_customer'].mean()
if pd.isna(otp_success):
    otp_success = 0.5 

otp_risk = 1 - otp_success
combined_risk = (0.3 * merchant_fraud_rate) + (0.3 * cust_fraud_rate) + (0.2 * otp_risk) + (0.2 * is_international)

#-------------------------------------------------------------------------------------------------------------------------------------

# A large, primary-colored button is much more inviting
if st.button("🚀 Run Risk Assessment", type="primary", use_container_width=True):
    
    # 2. Prepare Feature Vector
    input_data = pd.DataFrame({
        'payment_method' : [payment_method],
        'merchant_category' : [merchant_category],
        'authentication_method' : [authentication_method],
        'amount': [amount],
        'ip_address_risk_score': [ip_address_risk_score],
        'device_trust_score': [device_trust_score],
        'avg_amount_last_24h': [avg_amount_last_24h],
        'device_change_flag': [device_change_flag],
        'location_change_flag': [location_change_flag],
        'merchant_historical_fraud_rate': [merchant_historical_fraud_rate],
        'cust_txn_count': [cust_txn_count],
        'cust_fraud_count': [cust_fraud_count],
        'cust_fraud_rate': [cust_fraud_rate],
        'cust_avg_amt': [cust_avg_amt],
        'device_count': [device_count],
        'merchant_fraud_rate': [merchant_fraud_rate],
        'combined_risk': [combined_risk],
        'month': [month],
        'day': [day],
    })

    # 3. Prediction
    with st.spinner("Analyzing transaction patterns..."):
        prediction = pipeline.predict(input_data)[0]
        probability = pipeline.predict_proba(input_data)[0][1]

    # 4. Results Display
    st.markdown("---")
    st.subheader("📊 Risk Analysis Result")
    
    # Show off the engineered features alongside the result using st.metric
    met1, met2, met3 = st.columns(3)
    met1.metric("Fraud Probability", f"{probability:.2%}")
    met2.metric("Combined Risk Score", f"{combined_risk:.3f}")
    met3.metric("Customer Hist. Fraud Rate", f"{cust_fraud_rate:.1%}")
    
    st.progress(probability)
        
    if probability > 0.7:
        st.error("⚠️ **HIGH RISK DETECTED**")
        st.write("**Recommended Action:** Hard Block & Device Lock")
    elif probability > 0.4:
        st.warning("🟡 **MEDIUM RISK DETECTED**")
        st.write("**Recommended Action:** Trigger Mandatory OTP / Manual Review")
    else:
        st.success("✅ **LOW RISK**")
        st.write("**Recommended Action:** Approve Transaction")