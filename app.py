import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time

# --- 1. HARMONY OS SYSTEM CONTEXT ---
MASTER_CONTEXT = """
You are Harmony AI, the proprietary intelligence of Harmony OS for the T and C Estate.
Owner: Tony Carbone. Standard: 1420.405 MHz.
Directives: Professional, authoritative, and paramount.
"""

# --- 2. UI SETUP ---
st.set_page_config(page_title="Harmony OS", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050a0f; color: #00ffcc; }
    /* Padding to prevent bottom chat from covering lab content */
    .main .block-container { padding-bottom: 150px; }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session Memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 3. API HANDSHAKE ---
if "GEMINI_API_KEY" in st.secrets:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    MODEL_ID = "gemini-3.1-flash-lite-preview"
else:
    st.sidebar.error("🔑 Key Missing")
    st.stop()

# --- 4. SIDEBAR: THE MASTER TOGGLE ---
with st.sidebar:
    st.title("🏛️ HARMONY OS")
    st.write("---")
    # THIS IS YOUR BUTTON: Switch this to show/hide the AI
    ai_assistant_active = st.toggle("🛰️ Activate Harmony AI", value=False)
    st.write("---")
    if st.button("Clear Chat Memory"):
        st.session_state.messages = []
        st.rerun()

# --- 5. THE LAB (Always accessible) ---
st.title("🏛️ THE T AND C ESTATE")

# These stay at the top and are always visible
lab_tabs = st.tabs(["🚀 Null-G Simulation", "🛠️ System Diagnostics"])

with lab_tabs[0]:
    st.header("Null-G Propulsion Lab")
    m_in = st.number_input("Vessel Mass (kg)", value=50000, key="m_val")
    if st.button("EXECUTE MASS NEGATION"):
        st.metric("Effective Mass", f"{m_in * 1e-8:.8f} kg", delta="-99.999%")

with lab_tabs[1]:
    st.header("Master Diagnostics")
    st.line_chart(1420.405 + 0.005 * np.sin(np.linspace(0, 10, 100)))

# --- 6. CONDITIONAL CHAT INTERFACE ---
# Only runs if the Sidebar Toggle is 'ON'
if ai_assistant_active:
    st.divider()
    chat_container = st.container()
    
    # Display History
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # Bottom Pinned Input (Only visible when assistant is active)
    if prompt := st.chat_input("Query Harmony AI..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_container.chat_message("user"):
            st.markdown(prompt)
        
        with chat_container.chat_message("assistant"):
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=prompt,
                config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT)
            )
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
