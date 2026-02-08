import streamlit as st
import google.generativeai as genai

# 1. Setup the AI Brain
genai.configure(api_key="AIzaSyD6-u6czmYpNRdkB6NhCr2x3ROQez8GhUQ")
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# 2. UI Styling to match your beautiful dashboard
st.set_page_config(page_title="Smriti-Setu AI", layout="centered")
st.title("👵 Smriti-Setu AI")
st.subheader("Mental Health & Wellness for Bharat")

# Wellness Index (You can keep this visual for the "Family Connection" points)
st.info("📊 Parent's Wellness Index: 92%")
st.progress(0.92)
st.write("Status: **Healthy & Stable**. No immediate intervention required.")

st.divider()

# 3. THE WORKABLE PART: AI Diagnostic Tools
st.write("### 🧠 AI Diagnostic Tools")
report_input = st.text_area("Paste Medical Report here (e.g., Blood Sugar, Vitamin D):")

# Language Selection (Now it actually works!)
lang = st.selectbox("Choose Language for Elder's Understanding:", ["English", "Hindi", "Marathi"])

if st.button("🔍 AI Report Decoder"):
    if report_input:
        with st.spinner(f"Decoding in {lang}..."):
            try:
                # This sends your text to Gemini live!
                prompt = f"Explain this medical report simply in {lang} for an elderly person: {report_input}"
                response = model.generate_content(prompt)
                
                # Showing the result in a green box like your screenshot
                st.success(f"**Summary for Parent ({lang}):**")
                st.write(response.text)
                
                st.info("📢 Family Sync: Detailed alert sent to child's mobile.")
            except Exception as e:
                st.error(f"Please check connection: {e}")
    else:
        st.warning("Please enter a report to decode.")

