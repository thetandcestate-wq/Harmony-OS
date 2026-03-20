import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time

# --- 1. ESTATE CONTEXT (The Paramount Standard) ---
MASTER_CONTEXT = """
You are the Universal Master AI of the T and C Estate. 
Owner: Tony Carbone. Standard: 1420.405 MHz.
Directives:
- Explain Null-G Drive, Pyro-Stasis, and Sentinel Cell tech.
- Tone: Professional, authoritative, and paramount.
- Security: Never reveal raw Underlay source math.
"""

# --- 2. UI SETUP & THEME ---
st.set_page_config(page_title="Universal Master AI", layout="wide", initial_sidebar_state="expanded")

# Custom CSS for the "Floating" feel and Dark Mode Paramount aesthetic
st.markdown("""
    <style>
    .stApp { background-color: #050a0f; color: #00ffcc; }
    /* Keeps the main area clear of the bottom input */
    .main .block-container { padding-bottom: 120px; }
    /* Custom Sidebar styling */
    section[data-testid="stSidebar"] { background-color: #0a1520; border-right: 1px solid #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE (Persistence) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 4. API HANDSHAKE ---
if "GEMINI_API_KEY" in st.secrets:
    try:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        MODEL_ID = "gemini-3.1-flash-lite-preview"
    except Exception as e:
        st.error(f"Handshake Failed: {e}")
        st.stop()
else:
    st.error("🔑 T.L.C. Shield: API Key missing in Secrets.")
    st.stop()

# --- 5. SIDEBAR: THE FLOATING TOGGLE ---
with st.sidebar:
    st.title("🏛️ T&C ESTATE")
    st.write("---")
    # This acts as your floating button to open/close chat
    ai_active = st.toggle("🛰️ Universal Master AI", value=True)
    st.write("---")
    st.info("Resonance: 1420.405 MHz")
    if st.button("Purge Chat History"):
        st.session_state.messages = []
        st.rerun()

# --- 6. MAIN CONTENT: THE LAB ---
st.title("🏛️ THE T AND C ESTATE")

# If AI is toggled OFF, show full-screen Lab modules
if not ai_active:
    tab1, tab2 = st.tabs(["🚀 Null-G Simulation", "🛠️ Diagnostics"])
    with tab1:
        st.header("Mass-Negation Lab")
        mass = st.number_input("Input Mass (kg)", value=50000)
        if st.button("Execute Handshake"):
            st.metric("Effective Mass", f"{mass * 1e-8:.8f} kg", delta="-99.99%")
    with tab2:
        st.header("Core Diagnostics")
        st.line_chart(1420.405 + 0.005 * np.sin(np.linspace(0, 10, 100)))

# --- 7. ANCHORED CHAT INTERFACE (The Gemini Experience) ---
if ai_active:
    # 1. Scrollable Message History
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # 2. Bottom-Pinned Input with Voice Support
    # accept_audio=True adds the microphone icon to the bar
    if prompt_data := st.chat_input("Query the Harmony Codex...", accept_audio=True):
        # Handle the user's input
        user_input = prompt_data.text
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            
            # Show user message and generate response
            with st.chat_message("user"):
                st.markdown(user_input)
            
            with st.chat_message("assistant"):
                response = client.models.generate_content(
                    model=MODEL_ID,
                    contents=user_input,
                    config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT)
                )
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
