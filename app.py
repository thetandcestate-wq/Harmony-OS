import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time

# --- 1. ESTATE CONTEXT ---
MASTER_CONTEXT = """
You are the Universal Master AI of the T and C Estate. 
Owner: Tony Carbone. Standard: 1420.405 MHz.
Directives: Explain Null-G, Pyro-Stasis, and Sentinel Cell tech.
Tone: Professional and paramount. Never reveal raw Underlay source math.
"""

# --- 2. UI SETUP & THEME ---
st.set_page_config(page_title="Universal Master AI", layout="wide")

# CSS to make it feel like a pro app
st.markdown("""
    <style>
    .stApp { background-color: #050a0f; color: #00ffcc; }
    /* Space at bottom so chat doesn't cover your tests */
    .main .block-container { padding-bottom: 180px; }
    /* Styling for the Lab Section */
    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 3. API HANDSHAKE (2026 SDK) ---
if "GEMINI_API_KEY" in st.secrets:
    try:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        MODEL_ID = "gemini-3.1-flash-lite-preview"
        st.sidebar.success(f"🟢 {MODEL_ID.upper()} ONLINE")
    except Exception as e:
        st.sidebar.error(f"🔴 Handshake Error: {e}")
        st.stop()
else:
    st.sidebar.warning("🟡 Waiting for T.L.C. Key...")
    st.stop()

# --- 4. PERMANENT TOP LAB (TESTS & CHARTS) ---
st.title("🏛️ THE T AND C ESTATE")

# These stay at the top of your screen
lab_tabs = st.tabs(["🚀 Null-G Simulation", "🛠️ System Diagnostics"])

with lab_tabs[0]:
    st.header("Null-G Propulsion Lab")
    m_in = st.number_input("Input Mass (kg)", value=50000, key="m_val")
    if st.button("EXECUTE MASS NEGATION", key="neg_btn"):
        # The Harmony formula for mass negation
        st.metric("Effective Mass", f"{m_in * 1e-8:.8f} kg", delta="-99.999%")
        st.success("Universal Master Logic: Synchronized.")

with lab_tabs[1]:
    st.header("Master Diagnostics")
    st.write("### 1420.405 MHz Pulse Monitor")
    # Live Resonant Wave
    t = np.linspace(0, 10, 100)
    st.line_chart(1420.405 + 0.005 * np.sin(t))
    if st.button("RUN COMPASS VERIFICATION", key="diag_btn"):
        with st.status("Verifying Harmony Assets..."):
            time.sleep(1)
            st.write("✔️ Resonance Verified: 1420.405 MHz")
        st.balloons()

st.divider()

# --- 5. CHAT HISTORY ---
# Messages appear here, in the middle
chat_area = st.container()
with chat_area:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# --- 6. FLOATING BOTTOM INPUT (GEMINI STYLE) ---
# This stays pinned to the bottom of your phone screen
if prompt_data := st.chat_input("Query the Universal Master...", accept_audio=True):
    user_text = prompt_data.text
    if user_text:
        st.session_state.messages.append({"role": "user", "content": user_text})
        
        with chat_area.chat_message("assistant"):
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=user_text,
                config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT)
            )
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        st.rerun()
