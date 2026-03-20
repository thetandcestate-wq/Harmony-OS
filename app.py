import streamlit as st
import google.generativeai as genai

# --- CONNECTION STATUS ---
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # Test the key with a dummy call
        model = genai.GenerativeModel('gemini-1.5-flash')
        st.sidebar.success("🟢 API CONNECTED")
    except Exception as e:
        st.sidebar.error("🔴 API KEY INVALID")
else:
    st.sidebar.warning("🟡 WAITING FOR KEY...")

st.title("🏛️ Universal Master AI")
# ... (rest of your chat code)
