import streamlit as st
import google.generativeai as genai

# This key is your power source
genai.configure(api_key="AIzaSyD6-u6czmYpNRdkB6NhCr2x3ROQez8GhUQ")
# This '-latest' fix stops the 404 error
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.title("👵 Smriti-Setu AI")
st.subheader("Vernacular Health Bridge")

report = st.text_area("Paste Medical Report Text:")
lang = st.selectbox("Choose Language:", ["Hindi", "Marathi", "English"])

if st.button("Decode Now"):
    if report:
        response = model.generate_content(f"Explain this simply in {lang}: {report}")
        st.success(response.text)
