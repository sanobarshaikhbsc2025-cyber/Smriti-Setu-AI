import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="Smriti-Setu AI", page_icon="🏥")

# Header Section
st.title("🏥 Smriti-Setu AI")
st.subheader("Mental Health & Wellness for Bharat")

# 1. Wellness Index (The Dashboard)
st.info("### 📊 Parent's Wellness Index: 92%")
st.progress(92)
st.write("Status: **Healthy & Stable**. No immediate intervention required.")

st.markdown("---")
st.write("### 🤖 AI Diagnostic Tools (Offline Mode)")

# Create the two columns
col1, col2 = st.columns(2)

# --- SECTION 1: AI Report Decoder (Column 1) ---
with col1:
    st.write("**Medical Reports**")
    if st.button("🔍 AI Report Decoder"):
        with st.spinner('AI is analyzing your medical report...'):
            time.sleep(2) # Simulates AI thinking
        st.success("Summary: Blood sugar is normal, but Vitamin D is low. Recommendation: 15 mins of morning sunlight.")

# --- SECTION 2: Offline X-Ray Scan (Column 2) ---
with col2:
    st.write("**Imaging & Scans**")
    if st.button("📸 Offline X-Ray Scan"):
        with st.spinner('Analyzing scan on-device...'):
            time.sleep(3) # Simulates deep analysis
        st.warning("Detection: Minor congestion noted in lower left lung. Please consult a doctor within 48 hours.")

# 3. Vernacular Voice Feature
st.markdown("---")
st.write("### 🗣️ Vernacular Support")
language = st.selectbox("Choose Language:", ["Hindi", "Bengali", "Marathi", "Tamil", "English"])
st.success(f"AI Assistant is now ready to speak in **{language}**.")

# 4. Emergency Alert
st.markdown("---")
if st.button("🚨 SOS: ALERT CAREGIVER", type="primary", use_container_width=True):
    st.error("Emergency Alert Sent to Child's Phone via Firebase!")
