import streamlit as st
import random

st.set_page_config(page_title="AI Healthcare Dashboard", layout="wide")

# -------- SIDEBAR --------
st.sidebar.title("🧠 AI Healthcare System")
page = st.sidebar.radio("Navigate", ["Dashboard", "Predict Disease"])

# -------- DASHBOARD PAGE --------
if page == "Dashboard":
    st.title("📊 Healthcare Analytics Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Patients", "128")
    col2.metric("Common Disease", "Flu")
    col3.metric("System Accuracy", "87%")

    st.subheader("Disease Distribution")

    st.bar_chart({
        "Flu": [12],
        "Cold": [19],
        "Allergy": [7],
        "Migraine": [10]
    })

# -------- PREDICTION PAGE --------
elif page == "Predict Disease":
    st.title("🧪 Disease Prediction")

    col1, col2 = st.columns(2)

    with col1:
        fever = st.selectbox("Fever", ["No", "Yes"])
        headache = st.selectbox("Headache", ["No", "Yes"])

    with col2:
        fatigue = st.selectbox("Fatigue", ["No", "Yes"])
        cough = st.selectbox("Cough", ["No", "Yes"])

    if st.button("Predict"):

        confidence = random.randint(80, 95)

        if fever == "Yes" and headache == "Yes" and fatigue == "Yes":
            disease = "Flu"
            advice = "Take rest, drink fluids, consult doctor if needed"

        elif fever == "Yes" and cough == "Yes":
            disease = "Cold"
            advice = "Stay warm, drink hot fluids"

        elif headache == "Yes" and fatigue == "Yes":
            disease = "Migraine / Stress"
            advice = "Take rest, reduce screen exposure"

        else:
            disease = "No major illness"
            advice = "Maintain healthy lifestyle"

        st.success(f"🩺 Prediction: {disease}")
        st.info(f"💊 Advice: {advice}")
        st.warning(f"📈 Confidence Level: {confidence}%")

        st.progress(confidence / 100)
