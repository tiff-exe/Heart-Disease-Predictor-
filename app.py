import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.title("Heart Disease Prediction App")
st.write("Enter the patient's medical details below to predict heart disease risk.")

# 1. Load your saved model safely
import os

# 1. Define the exact path to your model file on your Desktop
# This forces Streamlit to look inside your true project folder no matter what!
model_path = r"C:\Users\Janet Owiti\Desktop\JN\Heart Disease Prediction\logistic_heart_model.pkl"

try:
    with open('logistic_heart_model.pkl', 'rb') as file:
        logistic_heart_model = pickle.load(file)
except FileNotFoundError:
    st.error(f"Could not find the model file at: {model_path}")

# 2. Form Layout for User Inputs
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=1, max_value=120, value=50)
    sex = st.selectbox("Sex", options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
    resting_bp = st.number_input("Resting Blood Pressure (mm Hg)", min_value=50, max_value=250, value=120)
    chol = st.number_input("Serum Cholestoral (mg/dl)", min_value=100, max_value=600, value=200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[1, 0], format_func=lambda x: "True" if x == 1 else "False")
    max_hr = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)

with col2:
    exang = st.selectbox("Exercise Induced Angina", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    oldpeak = st.number_input("ST Depression (oldpeak)", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
    vessels = st.selectbox("Number of Major Vessels Colored by Flourosopy (0-3)", options=[0, 1, 2, 3])
    
    # Categorical items that were One-Hot Encoded
    cp_type = st.selectbox("Chest Pain Type", options=["Typical angina", "Atypical angina", "Non-anginal pain", "Other / None"])
    rest_ecg = st.selectbox("Resting Electrocardiographic Results", options=["Normal", "ST-T wave abnormality", "Other"])
    slope_type = st.selectbox("Slope of the Peak Exercise ST Segment", options=["Flat", "Upsloping", "Downsloping / Other"])
    thal_type = st.selectbox("Thalassemia", options=["Normal", "Fixed Defect / No", "Reversable Defect"])

# 3. Create the 19 columns structure when the button is clicked
if st.button("Analyze Risk"):
    
    # Build an empty dictionary with all 19 features set to 0
    input_dict = {
        'age': age,
        'sex': sex,
        'resting_blood_pressure': resting_bp,
        'cholestoral': chol,
        'fasting_blood_sugar': fbs,
        'Max_heart_rate': max_hr,
        'exercise_induced_angina': exang,
        'oldpeak': oldpeak,
        'vessels_colored_by_flourosopy': vessels,
        'chest_pain_type_Atypical angina': 0,
        'chest_pain_type_Non-anginal pain': 0,
        'chest_pain_type_Typical angina': 0,
        'rest_ecg_Normal': 0,
        'rest_ecg_ST-T wave abnormality': 0,
        'slope_Flat': 0,
        'slope_Upsloping': 0,
        'thalassemia_No': 0,
        'thalassemia_Normal': 0,
        'thalassemia_Reversable Defect': 0
    }
    
    # Flip the 0 to 1 based on user selections
    if cp_type == "Atypical angina": input_dict['chest_pain_type_Atypical angina'] = 1
    elif cp_type == "Non-anginal pain": input_dict['chest_pain_type_Non-anginal pain'] = 1
    elif cp_type == "Typical angina": input_dict['chest_pain_type_Typical angina'] = 1
        
    if rest_ecg == "Normal": input_dict['rest_ecg_Normal'] = 1
    elif rest_ecg == "ST-T wave abnormality": input_dict['rest_ecg_ST-T wave abnormality'] = 1
        
    if slope_type == "Flat": input_dict['slope_Flat'] = 1
    elif slope_type == "Upsloping": input_dict['slope_Upsloping'] = 1
        
    if thal_type == "Fixed Defect / No": input_dict['thalassemia_No'] = 1
    elif thal_type == "Normal": input_dict['thalassemia_Normal'] = 1
    elif thal_type == "Reversable Defect": input_dict['thalassemia_Reversable Defect'] = 1

    
    # Convert the dictionary into a pandas DataFrame
    features_df = pd.DataFrame([input_dict])
    
    # Ensure strict column ordering matching your notebook layout
    correct_order = [
        'age', 'sex', 'resting_blood_pressure', 'cholestoral', 'fasting_blood_sugar', 
        'Max_heart_rate', 'exercise_induced_angina', 'oldpeak', 'vessels_colored_by_flourosopy', 
        'chest_pain_type_Atypical angina', 'chest_pain_type_Non-anginal pain', 
        'chest_pain_type_Typical angina', 'rest_ecg_Normal', 'rest_ecg_ST-T wave abnormality', 
        'slope_Flat', 'slope_Upsloping', 'thalassemia_No', 'thalassemia_Normal', 
        'thalassemia_Reversable Defect'
    ]
    features_df = features_df[correct_order]
    
    # Run the prediction
    prediction = logistic_heart_model.predict_proba(features_df)
    raw_score = prediction[0][1] # Assuming the model returns a single value for the risk score
    
    st.write("---")
    st.write(f"**Model Risk Score:** {raw_score:.4f}")
    
    if raw_score >=0.5:  # Adjust this threshold based on your model's calibration:  
        st.error("High Risk: The model indicates signs highly consistent with heart disease.")
    else:
        st.success("Low Risk: The medical metrics fall within normal/healthy boundaries.")