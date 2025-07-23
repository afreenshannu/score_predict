import streamlit as st
import requests

st.title("📃 score predictor 🤓")

study = st.slider("Study Time", 0, 10)
std = st.slider("Attended Days", 0, 80)
gen = st.selectbox("Gender", ["Male", "Female"])

gender = 1 if gen == "Male" else 0
if (st.button("Predict")):
    data = {
        "study_time": study,
        "attendance": std,
        "gender_male": gender

    }
    res = requests.post("https://score-predict-3.onrender.com/shannu", json=data)
    result = res.json()
    st.write("Here you GO:", result["Predicted_score"])
