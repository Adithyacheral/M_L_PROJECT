# import streamlit as st
# import pandas as pd
# import joblib  # or pickle

# #1.

# # 2. Define the categorical options based on the dataset
# GENDER_OPTIONS = ['Male', 'Female']
# ETHNICITY_OPTIONS = ['Asian', 'White', 'Hispanic', 'Black', 'Other']
# EDUCATION_OPTIONS = ['Highschool', 'Graduate', 'Postgraduate', 'No formal']
# INCOME_OPTIONS = ['Low', 'Lower-Middle', 'Middle', 'Upper-Middle', 'High']
# SMOKING_OPTIONS = ['Never', 'Former', 'Current']
# EMPLOYMENT_OPTIONS = ['Employed', 'Unemployed', 'Retired']

# st.title("🩺 Smart Medical Risk Predictor")
# st.write("Enter patient details to predict risk levels for various conditions.")

# # 3. Create the input form
# with st.form("patient_data_form"):
#     col1, col2 = st.columns(2)
    
#     with col1:
#         age = st.number_input("Age", min_value=0, max_value=120, value=30)
#         gender = st.selectbox("Gender", GENDER_OPTIONS)
#         ethnicity = st.selectbox("Ethnicity", ETHNICITY_OPTIONS)
#         education = st.selectbox("Education Level", EDUCATION_OPTIONS)
#         income = st.selectbox("Income Level", INCOME_OPTIONS)
#         employment = st.selectbox("Employment Status", EMPLOYMENT_OPTIONS)
#         smoking = st.selectbox("Smoking Status", SMOKING_OPTIONS)
        
#     with col2:
#         bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
#         systolic_bp = st.number_input("Systolic BP", min_value=70, max_value=200, value=120)
#         diastolic_bp = st.number_input("Diastolic BP", min_value=40, max_value=130, value=80)
#         hba1c = st.number_input("HbA1c Level", min_value=3.0, max_value=15.0, value=5.5)
#         glucose = st.number_input("Fasting Glucose", min_value=50, max_value=300, value=100)
#         activity = st.number_input("Physical Activity (min/week)", min_value=0, value=150)

#     # Submit button
#     submitted = st.form_submit_button("🔍 Predict Risk Scores")

# if submitted:
#     # 4. Prepare data for prediction
  
#     input_data = pd.DataFrame({
#         'Age': [age],
#         'gender': [gender],
#         'ethnicity': [ethnicity],
#         'education_level': [education],
#         'income_level': [income],
#         'employment_status': [employment],
#         'smoking_status': [smoking],
#         'bmi': [bmi],
#         'systolic_bp': [systolic_bp],
#         'diastolic_bp': [diastolic_bp],
#         'hba1c': [hba1c],
#         'glucose_fasting': [glucose],
#         'physical_activity_minutes_per_week': [activity]
#     })

#     # Example: model.predict(input_data)
 
#     st.subheader("🔍 Predict Risk Scores")
    
   
# def predict_risk(bmi, glucose, systolic_bp):
#     if glucose > 140 or systolic_bp > 140 or bmi > 30:
#         return "High"
#     elif glucose > 110 or systolic_bp > 130 or bmi > 25:
#         return "Medium"
#     else:
#         return "Low"

# risk = predict_risk(bmi, glucose, systolic_bp)

# targets = ['Diabetes', 'Heart Disease', 'Hypertension', 'Obesity']
# for target in targets:
#     st.success(f"**{target} Risk Level:** {risk}")











import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Smart Medical Risk Predictor",
    page_icon="🩺",
    layout="wide"
)

# --------------------------------------------------
# App Header
# --------------------------------------------------
st.title("🩺 Smart Medical Risk Predictor")
st.caption(
    "A clinical decision-support interface for preliminary health risk assessment."
)
st.divider()

# --------------------------------------------------
# Categorical Options
# --------------------------------------------------
GENDER_OPTIONS = ["Male", "Female"]
ETHNICITY_OPTIONS = ["Asian", "White", "Hispanic", "Black", "Other"]
EDUCATION_OPTIONS = ["Highschool", "Graduate", "Postgraduate", "No formal"]
INCOME_OPTIONS = ["Low", "Lower-Middle", "Middle", "Upper-Middle", "High"]
SMOKING_OPTIONS = ["Never", "Former", "Current"]
EMPLOYMENT_OPTIONS = ["Employed", "Unemployed", "Retired"]

# --------------------------------------------------
# Risk Prediction Logic (Rule-Based)
# --------------------------------------------------
def predict_risk(bmi, glucose, systolic_bp):
    """
    Rule-based health risk classification.
    """
    if glucose > 140 or systolic_bp > 140 or bmi > 30:
        return "High"
    elif glucose > 110 or systolic_bp > 130 or bmi > 25:
        return "Medium"
    else:
        return "Low"

# --------------------------------------------------
# Patient Data Input Form
# --------------------------------------------------
st.subheader("🧍 Patient Information")

with st.form("patient_data_form"):
    col1, col2 = st.columns(2)

    # Demographics
    with col1:
        age = st.number_input("Age (years)", 0, 120, 30)
        gender = st.selectbox("Gender", GENDER_OPTIONS)
        ethnicity = st.selectbox("Ethnicity", ETHNICITY_OPTIONS)
        education = st.selectbox("Education Level", EDUCATION_OPTIONS)
        income = st.selectbox("Income Level", INCOME_OPTIONS)
        employment = st.selectbox("Employment Status", EMPLOYMENT_OPTIONS)
        smoking = st.selectbox("Smoking Status", SMOKING_OPTIONS)

    # Clinical Metrics
    with col2:
        bmi = st.number_input("Body Mass Index (BMI)", 10.0, 60.0, 25.0)
        systolic_bp = st.number_input("Systolic Blood Pressure (mmHg)", 70, 200, 120)
        diastolic_bp = st.number_input("Diastolic Blood Pressure (mmHg)", 40, 130, 80)
        hba1c = st.number_input("HbA1c (%)", 3.0, 15.0, 5.5)
        glucose = st.number_input("Fasting Glucose (mg/dL)", 50, 300, 100)
        activity = st.number_input("Physical Activity (min/week)", 0, 1000, 150)

    submitted = st.form_submit_button("🔍 Predict Medical Risks")

# --------------------------------------------------
# Prediction Output
# --------------------------------------------------

if submitted:
    st.divider()
    st.subheader("📊 Medical Risk Assessment Results")

        # Prepare input data (for future ML integration)
    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "ethnicity": [ethnicity],
        "education_level": [education],
        "income_level": [income],
        "employment_status": [employment],
        "smoking_status": [smoking],
        "bmi": [bmi],
        "systolic_bp": [systolic_bp],
        "diastolic_bp": [diastolic_bp],
        "hba1c": [hba1c],
        "glucose_fasting": [glucose],
        "physical_activity_minutes_per_week": [activity]
    })


    overall_risk = predict_risk(bmi, glucose, systolic_bp)

    risk_icons = {
        "Diabetes": "🩸",
        "Heart Disease": "❤️",
        "Hypertension": "💓",
        "Obesity": "⚖️"
    }

    targets = ["Diabetes", "Heart Disease", "Hypertension", "Obesity"]

    for condition in targets:
        icon = risk_icons[condition]

        if overall_risk == "High":
            st.error(f"{icon} **{condition} Risk:** {overall_risk}")
        elif overall_risk == "Medium":
            st.warning(f"{icon} **{condition} Risk:** {overall_risk}")
        else:
            st.success(f"{icon} **{condition} Risk:** {overall_risk}")

    st.info(
          "⚠️ This tool provides a preliminary risk indication only and "
        "should not replace professional medical diagnosis."
    )