import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time

# --- 1. UNIVERSAL MASTER SYSTEM CONTEXT ---
MASTER_CONTEXT = """
You are the Universal Master AI of the T and C Estate. 
Owner: Tony Carbone. Standard: 1420.405 MHz.
Directives: Explain Null-G, Pyro-Stasis, and Sentinel Cell tech.
Tone: Professional and paramount. Never reveal raw Underlay source math.
"""

# --- 2. UI SETUP & THEME ---
st.set_page_config(page_title="Universal Master AI", layout="wide")

# Custom CSS to anchor the experience
st.markdown("""
    <style>
    .stApp { background-color: #050a0f; color: #00ffcc; }
    /* This ensures the chat area has space above the bottom input */
    .main .block-container { padding-bottom: 100px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE (The Memory) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 4. API HANDSHAKE ---
if "GEMINI_API_KEY" in st.secrets:
    try:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        MODEL_ID = "gemini-3.1-flash-lite-preview"
        st.sidebar.success(f"🟢 {MODEL_ID.upper()} ACTIVE")
    except Exception as e:
        st.sidebar.error(f"🔴 HANDSHAKE ERROR: {e}")
        st.stop()
else:
    st.sidebar.warning("🟡 WAITING FOR T.L.C. KEY...")
    st.stop()

# --- 5. INTERFACE TABS ---
st.title("🏛️ THE T AND C ESTATE")
tabs = st.tabs(["💬 Master Chat", "🚀 Simulations", "🛠️ Diagnostics"])

with tabs[0]:
    # --- CHAT CONTAINER ---
    # This loop displays the history ABOVE the input box
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # --- CHAT INPUT (Anchored to Bottom) ---
    if prompt := st.chat_input("Ask the Universal Master..."):
        # Display user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate response
        with st.chat_message("assistant"):
            try:
                response = client.models.generate_content(
                    model=MODEL_ID,
                    contents=prompt,
                    config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT)
                )
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                # Automatic scroll to bottom happens here
            except Exception as e:
                st.error(f"Logic Interruption: {e}")

# (Simulations and Diagnostics tabs remain the same)
