import streamlit as st
import google.generativeai as genai

# 1. DIRECT API CONFIGURATION (Bypasses Secrets)
# This ensures your app works for the Ideathon registration immediately!
API_KEY = "AIzaSyD6-u6czmYpNRdkB6NhCr2x3ROQez8GhUQ"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# 2. APP INTERFACE SETTINGS
st.set_page_config(page_title="Smriti-Setu AI", page_icon="👵", layout="centered")

# Custom Styling for the "Look"
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("👵 Smriti-Setu AI")
st.subheader("Your Vernacular Health Bridge")

# 3. TABS FOR FEATURES
tab1, tab2 = st.tabs(["📄 Report Decoder", "🚨 SOS Emergency"])

with tab1:
    st.write("Upload or paste your medical report details below:")
    
    report_text = st.text_area("Paste report text (e.g., HbA1c: 8.5%):", height=150, placeholder="Type or paste medical details here...")
    
    col1, col2 = st.columns(2)
    with col1:
        target_lang = st.selectbox("Choose your language:", ["Hindi", "Marathi", "English", "Gujarati", "Tamil"])
    
    if st.button("Decode Now"):
        if report_text:
            with st.spinner('Simplifying for you...'):
                try:
                    # The Prompt for Gemini 1.5 Flash
                    prompt = f"""
                    You are a helpful medical assistant for elderly people in India. 
                    Explain the following medical data in very simple, reassuring {target_lang}. 
                    Avoid hard medical jargon. Tell them what it means and one simple next step.
                    Data: {report_text}
                    """
                    response = model.generate_content(prompt)
                    st.success(f"### Meaning in {target_lang}:")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Technical Error: {e}")
        else:
            st.warning("Please enter some text first!")

with tab2:
    st.error("### 🚨 Emergency Assistance")
    st.write("If this is a life-threatening emergency, please call **108** immediately.")
    if st.button("SEND SOS TO FAMILY"):
        st.write("✅ SOS Alert Sent to saved emergency contacts (Simulation)")

st.divider()
st.caption("Disclaimer: This is an AI tool for educational purposes. Always consult a real doctor for medical advice.")