import streamlit as st
import requests

st.title("Emotion Analyzer")
text = st.text_input("Analyze ANYONES emotion by entering their text here:")

if st.button("Analyze"):
    if text:
        response = requests.post("http://127.0.0.1:8000/predict/", json={"text": text})
        result = response.json()
        st.success(f"Predicted Emotion: {result['emotion']}")
    else:
        st.warning("Please enter some text to analyze.")