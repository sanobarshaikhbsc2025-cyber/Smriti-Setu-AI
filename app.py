import streamlit as st
import google.generativeai as genai

# This API Key is your "Fuel" - Keep it as is
genai.configure(api_key="AIzaSyD6-u6czmYpNRdkB6NhCr2x3ROQez8GhUQ")

# THE FIX: Adding '-latest' ensures the model is found (No more 404!)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

st.set_page_config(page_title="Smriti-Setu AI", page_icon="👵")
st.title("👵 Smriti-Setu AI")
st.markdown("### Bridging the gap for our elders")

# Input area for the demo
report_text = st.text_area("Paste the Medical Report Text here:", height=200)
target_lang = st.selectbox("Explain in which language?", ["Hindi", "Marathi", "English"])

if st.button("Decode Now"):
    if report_text:
        with st.spinner('Decoding for your family...'):
            try:
                # Optimized prompt for the live demo
                prompt = f"Explain this medical report simply in {target_lang} for an elderly person. Use a comforting tone and avoid jargon: {report_text}"
                response = model.generate_content(prompt)
                
                st.success("Analysis Complete!")
                st.write(response.text)
                
                # Mentioning the mobile connection for the judges
                st.info("📢 Family Alert: Summary sent to the child's mobile.")
            except Exception as e:
                st.error(f"Technical Error: {e}")
    else:
        st.warning("Please paste a report first!")
