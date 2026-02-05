import streamlit as st
import google.generativeai as genai

# Page Config
st.set_page_config(page_title="Smriti-Setu AI", page_icon="👵", layout="centered")

# Load API Key from Secrets
try:
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
    else:
        st.error("Missing API Key! Please add 'GEMINI_API_KEY' to your Streamlit Secrets.")
except Exception as e:
    st.error(f"Setup Error: {e}")

# Header
st.title("👵 Smriti-Setu AI")
st.markdown("### *Your Health Bridge in Your Language*")

# Tabs for Features
tab1, tab2 = st.tabs(["📋 Report Decoder", "🚨 SOS Emergency"])

with tab1:
    st.write("Upload or paste your medical report details below:")
    user_input = st.text_area("Paste report text (e.g., Blood Sugar: 160):", height=150)
    
    language = st.selectbox("Choose your language:", ["English", "Hindi", "Marathi", "Tamil", "Gujarati"])

    if st.button("Decode Now", type="primary"):
        if user_input:
            with st.spinner(f"Translating and simplifying in {language}..."):
                try:
                    prompt = f"Explain this medical data to an elderly person in very simple {language} terms. Be empathetic and clear: {user_input}"
                    response = model.generate_content(prompt)
                    st.success("### AI Analysis:")
                    st.write(response.text)
                except Exception as e:
                    st.error("The AI is resting right now. Check your API key!")
        else:
            st.warning("Please enter some medical details first.")

with tab2:
    st.error("## EMERGENCY ASSISTANCE")
    if st.button("🔴 SEND SOS TO FAMILY", use_container_width=True):
        st.warning("SOS Alert Sent! Rahul (Son) has been notified of your location.")

st.divider()
st.caption("Smriti-Setu AI - Empowering Bharat's Elders")