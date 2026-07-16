import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

# Set page config
st.set_page_config(
    page_title="Bank Customer Churn Prediction",
    page_icon="🏦",
    layout="wide"
)

# Title and description
st.title("🏦 Bank Customer Churn Prediction")
st.markdown("### Predict whether a customer will exit the bank")

# Load the trained model
@st.cache_resource
def load_model():
    try:
        with open('model.pkl', 'rb') as file:
            model = pickle.load(file)
        with open('scaler.pkl', 'rb') as file:
            scaler = pickle.load(file)
        return model, scaler
    except:
        st.error("Model files not found. Please train the model first.")
        return None, None

model, scaler = load_model()

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    st.subheader("Customer Demographics")
    
    credit_score = st.slider("Credit Score", 300, 850, 650)
    age = st.slider("Age", 18, 100, 35)
    
    geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
    gender = st.selectbox("Gender", ["Female", "Male"])
    
with col2:
    st.subheader("Account Information")
    
    tenure = st.slider("Tenure (years)", 0, 10, 5)
    balance = st.number_input("Balance", 0, 300000, 50000)
    num_of_products = st.slider("Number of Products", 1, 4, 2)
    
    has_cr_card = st.selectbox("Has Credit Card", [0, 1])
    is_active_member = st.selectbox("Is Active Member", [0, 1])
    estimated_salary = st.number_input("Estimated Salary", 0, 200000, 50000)

# Feature Engineering Function
def engineer_features(data):
    # Create engineered features
    data['Balance_To_Salary_Ratio'] = data['Balance'] / (data['EstimatedSalary'] + 1)
    data['Product_Density'] = data['NumOfProducts'] / (data['Tenure'] + 1)
    data['Engagement_Product_Interaction'] = data['IsActiveMember'] * data['NumOfProducts']
    data['Age_Tenure_Interaction'] = data['Age'] * (data['Tenure'] + 1)
    
    # Age groups
    if data['Age'].values[0] <= 30:
        data['Age_Group_Middle_Aged'] = 0
        data['Age_Group_Senior'] = 0
        data['Age_Group_Elderly'] = 0
    elif data['Age'].values[0] <= 45:
        data['Age_Group_Middle_Aged'] = 1
        data['Age_Group_Senior'] = 0
        data['Age_Group_Elderly'] = 0
    elif data['Age'].values[0] <= 60:
        data['Age_Group_Middle_Aged'] = 0
        data['Age_Group_Senior'] = 1
        data['Age_Group_Elderly'] = 0
    else:
        data['Age_Group_Middle_Aged'] = 0
        data['Age_Group_Senior'] = 0
        data['Age_Group_Elderly'] = 1
    
    return data

# Prediction button
if st.button("🔮 Predict Churn", type="primary"):
    if model is not None:
        # Create input dataframe
        input_data = pd.DataFrame({
            'CreditScore': [credit_score],
            'Geography': [geography],
            'Gender': [gender],
            'Age': [age],
            'Tenure': [tenure],
            'Balance': [balance],
            'NumOfProducts': [num_of_products],
            'HasCrCard': [has_cr_card],
            'IsActiveMember': [is_active_member],
            'EstimatedSalary': [estimated_salary]
        })
        
        # Engineer features
        input_data = engineer_features(input_data)
        
        # Encode categorical variables
        # Geography encoding
        input_data['Geography_Germany'] = 1 if geography == 'Germany' else 0
        input_data['Geography_Spain'] = 1 if geography == 'Spain' else 0
        
        # Gender encoding
        input_data['Gender_Male'] = 1 if gender == 'Male' else 0
        
        # Drop original categorical columns
        input_data = input_data.drop(['Geography', 'Gender'], axis=1)
        
        # Select features in correct order
        feature_columns = [
            'CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
            'HasCrCard', 'IsActiveMember', 'EstimatedSalary',
            'Balance_To_Salary_Ratio', 'Product_Density',
            'Engagement_Product_Interaction', 'Age_Tenure_Interaction',
            'Geography_Germany', 'Geography_Spain', 'Gender_Male',
            'Age_Group_Middle_Aged', 'Age_Group_Senior', 'Age_Group_Elderly'
        ]
        
        input_data = input_data[feature_columns]
        
        # Scale features
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)
        prediction_proba = model.predict_proba(input_scaled)
        
        # Display results
        st.markdown("---")
        st.subheader("📊 Prediction Results")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if prediction[0] == 1:
                st.error("### ⚠️ Customer is likely to CHURN")
            else:
                st.success("### ✅ Customer is likely to STAY")
        
        with col2:
            st.metric("Churn Probability", f"{prediction_proba[0][1]:.1%}")
        
        with col3:
            st.metric("Stay Probability", f"{prediction_proba[0][0]:.1%}")
        
        # Risk assessment
        churn_prob = prediction_proba[0][1]
        if churn_prob > 0.7:
            risk_level = "🔴 High Risk"
            recommendation = "Immediate intervention recommended. Consider personalized retention offers."
        elif churn_prob > 0.4:
            risk_level = "🟡 Medium Risk"
            recommendation = "Monitor closely. Engage with customer through satisfaction surveys."
        else:
            risk_level = "🟢 Low Risk"
            recommendation = "Continue regular engagement. Customer appears satisfied."
        
        st.markdown(f"### Risk Level: {risk_level}")
        st.info(recommendation)

# Add information about the app
st.markdown("---")
st.markdown("""
### About This App
This application uses machine learning to predict bank customer churn based on various factors including:
- Customer demographics (Age, Geography, Gender)
- Account information (Balance, Products, Credit Card, Activity)
- Financial indicators (Credit Score, Estimated Salary)

The model is trained on historical data to identify patterns that indicate a customer is likely to leave the bank.
""")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit")
