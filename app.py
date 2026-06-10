import streamlit as st
import requests
import joblib
model = joblib.load('pipeline.pickle')

st.title("Emotion Analyzer")
text = st.text_input("Analyze ANYONES emotion by entering their text here:")

if st.button("Analyze"):
    if text:
        prediction = model.predict([text])[0]
        st.success(f"Emotion:{prediction.upper()}")
    else:
        st.warning("Please enter some text to analyze.")
