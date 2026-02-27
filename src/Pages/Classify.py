import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Predict")

original_df = pd.read_csv(r'C:\Users\mabin\Desktop\DataScienceClassNotes\Career247_Capstone_Project\Fraud_Detection_Project\data\raw\transactions_fraud.csv')

df = pickle.load(open('models\df.pkl', 'rb'))

pipeline = pickle.load(open(r'C:\Users\mabin\Desktop\DataScienceClassNotes\Career247_Capstone_Project\Fraud_Detection_Project\models\pipeline.pkl', 'rb'))

st.dataframe(df)

st.header("Enter Your Inputs")

# # -----------------------------------------------------------------------------------------------------------------------------

df['transaction_date'] = pd.to_datetime(df['transaction_date'])

# Customer ID
customer_id = st.number_input("Customer ID")

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



# if customer_id in df['customer_id'].unique():
    
# Avrage Amount Last 24h
avg_amount_last_24h = df.loc[df['customer_id'] == customer_id, 'avg_amount_last_24h'].max()


# Merchant Historical Fraud Rate
merchant_historical_fraud_rate = df.loc[df['customer_id'] == customer_id, 'merchant_historical_fraud_rate'].mean()


# Customer Transaction Count
cust_txn_count = int(df.loc[df['customer_id'] == customer_id, 'customer_id'].count())

# Customer Fraud Count
cust_fraud_count = df.loc[df['customer_id'] == customer_id, 'is_fraud'].sum()

# Customer Fraud rate
cust_fraud_rate = df.loc[df['customer_id'] == customer_id, 'is_fraud'].mean()
if pd.notna(cust_fraud_rate):
    cust_fraud_rate = int(cust_fraud_rate)
else:
    cust_fraud_rate = 0

# Customer Average Amount
cust_avg_amt = df.loc[df['customer_id'] == customer_id, 'amount'].mean()


# Device Count
device_count = df.loc[df['customer_id'] == customer_id, 'device_count'].max()
if pd.notna(device_count):
    device_count = int(device_count)
else:
    device_count = 0

# Merchant Fruad Rate
merchant_fraud_rate = df.loc[df['customer_id'] == customer_id, 'merchant_fraud_rate'].mean()


# Combined Risk
combined_risk = df.loc[df['customer_id'] == customer_id, 'combined_risk'].mean()




# Day and Months
day = int(df['transaction_date'].dt.day.mean())
month = int(df['transaction_date'].dt.month.mean())







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
#          'transaction_amt :  ',amount, 
#          'ip_ad_score :  ',ip_address_risk_score, 
#          'device_trust_score :  ',device_trust_score, 
#          'device_flag :  ',device_change_flag,
#          'location_flag :  ',location_change_flag,
#          'device_count :  ',device_count, 
#          'cust_avg_amt :  ',cust_avg_amt, 
#          'cust_fraud_rate :  ', cust_fraud_rate, 
#          'cust_farud_count :  ',cust_fraud_count,
#          'cust_txn_count :  ',cust_txn_count,
#          'avg_amount_last_24h :  ',avg_amount_last_24h,
#          'merchant_fraud_rate :  ',merchant_fraud_rate,
#          'merchant_historical_fraud_rate :  ',merchant_historical_fraud_rate,
#          'combined_risk :  ', combined_risk,
#          'day :  ', day,
#          'month :  ', month)

if st.button("Run Risk Assessment"):

    # 2. Prepare Feature Vector (Must match training column order)
    input_data = pd.DataFrame({
        'customer_id' : [customer_id],
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
        # Add all other features your model was trained on...
    })

    # 3. Prediction
    prediction = pipeline.predict(input_data)[0]
    probability = pipeline.predict_proba(input_data)[0][1]

    # 4. Results Display
    st.subheader("Risk Analysis Result")
        
    if probability > 0.7:
        st.error(f"⚠️ HIGH RISK: Fraud Probability {probability:.2%}")
        st.write("**Recommended Action:** Hard Block & Device Lock")
    elif probability > 0.4:
        st.warning(f"🟡 MEDIUM RISK: Fraud Probability {probability:.2%}")
        st.write("**Recommended Action:** Trigger Mandatory OTP / Manual Review")
    else:
        st.success(f"✅ LOW RISK: Fraud Probability {probability:.2%}")
        st.write("**Recommended Action:** Approve Transaction")

    # Visualization of Feature Importance or Risk
    st.progress(probability)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
