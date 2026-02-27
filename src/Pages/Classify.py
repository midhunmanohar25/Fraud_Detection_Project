import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Predict")

original_df = pd.read_csv(r'C:\Users\mabin\Desktop\DataScienceClassNotes\Career247_Capstone_Project\Fraud_Detection_Project\data\raw\transactions_fraud.csv')

df = pickle.load(open(r'C:\Users\mabin\Desktop\DataScienceClassNotes\Career247_Capstone_Project\Fraud_Detection_Project\models\df.pkl', 'rb'))

pipeline = pickle.load(open(r'C:\Users\mabin\Desktop\DataScienceClassNotes\Career247_Capstone_Project\Fraud_Detection_Project\models\pipeline.pkl', 'rb'))

st.dataframe(df)

st.header("Enter Your Inputs")

# # -----------------------------------------------------------------------------------------------------------------------------

# Customer ID
customer_id = st.number_input(
    "Customer ID",
    min_value=int(original_df['customer_id'].min()),
    max_value=int(original_df['customer_id'].max()),
    step=1
)

customer_id = int(customer_id)


# Payment Method
payment_method = st.selectbox('Payment Method',df['payment_method'].unique().tolist())


# Merchant Category
merchant_category = st.selectbox('Merchant Category', df['merchant_category'].unique().tolist())


# Authentication Method
authentication_method = st.selectbox('Authentication Method', df['authentication_method'].unique().tolist())


# Transaction Amount
amount = st.number_input("Transaction Amount", min_value=0.0)


# IP Risk Score
ip_address_risk_score = st.slider("IP Risk Score", 0.0, 1.0)


# Device Trust Score
device_trust_score = st.slider("Device Trust Score", 0.0, 1.0)




# Device Count
device_count = original_df.loc[original_df['customer_id'] == customer_id, 'device_id'].nunique()

# Customer Average Amount
cust_avg_amt = original_df.loc[original_df['customer_id'] == customer_id, 'amount'].mean()



# Customer Fraud rate
cust_fraud_rate = df.loc[original_df['customer_id'] == customer_id, 'is_fraud'].mean()


# Customer Fraud Count
cust_fraud_count = original_df.loc[original_df['customer_id'] == customer_id, 'is_fraud'].sum()


# Customer Transaction Count
cust_txn_count = original_df.loc[original_df['customer_id'] == customer_id, 'transaction_id'].count()




# Device Change Flag
device_change = st.radio("Is this a new device?", ["No", "Yes"])
if device_change == "Yes":
    device_change_flag = 1
else:
    device_change_flag = 0

# Location Change Flag
location_change = st.radio("Is location changed?", ["No", "Yes"])
if location_change == "Yes":
    location_change_flag = 1
else:
    location_change_flag = 0




# ---------------------------------------------------------------------------------------------------------------------------------
# # Transaction Date
# transaction_date = st.date_input("Transaction Date", )


# # Avg Amount Last 24h
# avg_amount_last_24h = df.loc[df['customer_id'] == customer_id, 'avg_amount_last_24h'].mean()


# Transaction Date
# transaction_date = st.date_input("Transaction Date", )


# if st.button("Predict"):
    
#     data = [['UPI',	'Electronics',	'OTP',	16807.26,	0.752472,	0.729953,	10895.68,	0,	0,	0.139440,	10,	1,	0.166667,	10000.218000,	10,	0.042169,	0.096758,	2,	12]]

#     columns = ['payment_method',	'merchant_category',	'authentication_method',	'amount',	'ip_address_risk_score',	'device_trust_score',	
#                'avg_amount_last_24h',	'device_change_flag',	'location_change_flag',	'merchant_historical_fraud_rate',	'cust_txn_count',	
#                'cust_fraud_count',	'cust_fraud_rate',	'cust_avg_amt',	'device_count',	'merchant_fraud_rate',	'combined_risk',	'month',	'day']



#     one_df = pd.DataFrame(data, columns=columns)
    
#     base_predict = pipeline.predict(one_df)[0]
    
#     st.success(base_predict)



# st.write('cust_id :  ',customer_id,
#          'payment_method:  ',payment_method,
#          'merchant_cat :  ',merchant_category,
#          'authent_method :  ',authentication_method,
#          'transaction_amt :  ',transaction_amt, 
#          'ip_ad_score :  ',ip_address_risk_score, 
#          'device_trust_score :  ',device_trust_score, 
#          'device_flag :  ',device_change_flag,
#          'location_flag :  ',location_change_flag,
#          'device_count :  ',device_count, 
#          'cust_avg_amt :  ',cust_avg_amt, 
#          'cust_fraud_rate :  ', cust_fraud_rate, 
#          'cust_farud_count :  ',cust_fraud_count,
#          'cust_txn_count :  ',cust_txn_count)

# if st.button("Run Risk Assessment"):
#     # 1. Feature Engineering (Derived on the fly)
#     amt_ratio = amount / (cust_avg_amt + 1)
#     otp_risk = 1 - otp_success_rate
        
#     # 2. Prepare Feature Vector (Must match training column order)
#     input_data = pd.DataFrame({
#         'amount': [amount],
#         'ip_address_risk_score': [ip_risk],
#         'device_trust_score': [device_trust],
#         'is_international': [1 if is_international else 0],
#         'amt_ratio': [amt_ratio],
#         'otp_risk': [otp_risk],
#         'past_fraud_count_customer': [past_fraud_count],
#         'new_device_flag': [1 if new_device else 0]
#         # Add all other features your model was trained on...
#     })

#     # 3. Prediction
#     prediction = model.predict(input_data)[0]
#     probability = model.predict_proba(input_data)[0][1]

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
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
