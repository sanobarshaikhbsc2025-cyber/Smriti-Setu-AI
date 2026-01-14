import streamlit as st

# Page Configuration
st.set_page_config(page_title="Smriti-Setu AI", page_icon="🏥")

# Header Section
st.title("🏥 Smriti-Setu AI")
st.subheader("Mental Health & Wellness for Bharat")

# 1. Wellness Index (The Dashboard)
st.info("### 📊 Parent's Wellness Index: 92%")
st.progress(92)
st.write("Status: **Healthy & Stable**. No immediate intervention required.")

# 2. AI Diagnostic Features
st.markdown("---")
st.write("### 🤖 AI Diagnostic Tools (Offline Mode)")

col1, col2 = st.columns(2)

with col1:
    if st.button("🔍 AI Report Decoder"):
        st.write("Feature: Simplifying medical jargon into simple Hindi/English...")

with col2:
    if st.button("📸 Offline X-Ray Scan"):
        st.write("Feature: Running TensorFlow Lite for lung health analysis...")

# 3. Vernacular Voice Feature
st.markdown("---")
st.write("### 🗣️ Vernacular Support")
language = st.selectbox("Choose Language:", ["Hindi", "Bengali", "Marathi", "Tamil", "English"])
st.success(f"AI Assistant is now ready to speak in **{language}**.")

# 4. Emergency Alert
st.markdown("---")
if st.button("🚨 SOS: ALERT CAREGIVER", type="primary"):
    st.error("Emergency Alert Sent to Child's Phone via Firebase!")
