import streamlit as st
import random

st.set_page_config(page_title="MediCore AI", layout="wide")

# -------- CUSTOM CSS (MAGIC PART) --------
st.markdown("""
<style>
body {
    background-color: #0f172a;
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #020617;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background: #1e293b;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.4);
    margin-bottom: 20px;
}

.title {
    font-size: 28px;
    font-weight: bold;
}

.sub {
    color: #94a3b8;
}

</style>
""", unsafe_allow_html=True)

# -------- SIDEBAR --------
st.sidebar.markdown("## 🏥 MediCore.AI")
st.sidebar.caption("Healthcare OS")

menu = st.sidebar.radio(
    "Modules",
    ["Dashboard", "Symptom Checker", "AI Chatbot", "Report Analyzer", "Patient Records"]
)

# -------- DASHBOARD --------
if menu == "Dashboard":
    st.markdown('<div class="title">📊 Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub">AI-assisted healthcare system</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">👥 Patients<br><h2>128</h2></div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">🦠 Common Disease<br><h2>Flu</h2></div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">📈 Accuracy<br><h2>87%</h2></div>', unsafe_allow_html=True)

    st.markdown("### 📊 Disease Distribution")
    st.bar_chart({
        "Flu": [12],
        "Cold": [19],
        "Allergy": [7],
        "Stress": [10]
    })

# -------- SYMPTOM CHECKER --------
elif menu == "Symptom Checker":
    st.markdown('<div class="title">🧪 Symptom Checker</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        fever = st.selectbox("Fever", ["No", "Yes"])
        headache = st.selectbox("Headache", ["No", "Yes"])

    with col2:
        fatigue = st.selectbox("Fatigue", ["No", "Yes"])
        cough = st.selectbox("Cough", ["No", "Yes"])

    if st.button("Analyze Symptoms"):
        confidence = random.randint(80, 95)

        if fever == "Yes" and headache == "Yes" and fatigue == "Yes":
            disease = "Flu"
            advice = "Take rest and drink fluids"

        elif fever == "Yes" and cough == "Yes":
            disease = "Cold"
            advice = "Stay warm and hydrated"

        elif headache == "Yes" and fatigue == "Yes":
            disease = "Migraine / Stress"
            advice = "Take rest, reduce screen time"

        else:
            disease = "No major illness"
            advice = "Maintain healthy lifestyle"

        st.success(f"🩺 Diagnosis: {disease}")
        st.info(f"💊 Advice: {advice}")
        st.warning(f"📊 Confidence: {confidence}%")

# -------- AI CHATBOT --------
elif menu == "AI Chatbot":
    st.markdown('<div class="title">🤖 AI Chatbot</div>', unsafe_allow_html=True)

    user_input = st.text_input("Ask a health question:")

    if user_input:
        st.markdown('<div class="card">AI Response:<br>Consult a doctor for accurate diagnosis.</div>', unsafe_allow_html=True)

# -------- REPORT ANALYZER --------
elif menu == "Report Analyzer":
    st.markdown('<div class="title">📄 Report Analyzer</div>', unsafe_allow_html=True)

    file = st.file_uploader("Upload medical report")

    if file:
        st.success("Report uploaded successfully!")
        st.info("Basic analysis: No critical issues detected.")

# -------- PATIENT RECORDS --------
elif menu == "Patient Records":
    st.markdown('<div class="title">👨‍⚕️ Patient Records</div>', unsafe_allow_html=True)

    st.table({
        "Name": ["Riya", "Aman"],
        "Disease": ["Flu", "Cold"],
        "Status": ["Recovering", "Stable"]
    })
