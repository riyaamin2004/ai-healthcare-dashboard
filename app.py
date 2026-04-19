import streamlit as st

st.set_page_config(page_title="AI Healthcare Dashboard")

st.title("🧠 AI Healthcare Dashboard")

st.metric("Total Patients Checked", "120")
st.metric("Common Disease", "Flu")
st.metric("System Accuracy", "85%")

st.write("### Enter Symptoms")

fever = st.selectbox("Fever", ["No", "Yes"])
headache = st.selectbox("Headache", ["No", "Yes"])
fatigue = st.selectbox("Fatigue", ["No", "Yes"])
cough = st.selectbox("Cough", ["No", "Yes"])

if st.button("Predict"):

    if fever == "Yes" and headache == "Yes" and fatigue == "Yes":
        disease = "Flu"
        advice = "Take rest and drink fluids"

    elif fever == "Yes" and cough == "Yes":
        disease = "Cold"
        advice = "Stay warm and hydrated"

    elif headache == "Yes" and fatigue == "Yes":
        disease = "Migraine / Stress"
        advice = "Take rest and reduce screen time"

    else:
        disease = "No major illness"
        advice = "Stay healthy"

    st.success(f"Prediction: {disease}")
    st.info(f"Advice: {advice}")
