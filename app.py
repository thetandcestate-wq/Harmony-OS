import streamlit as st
import google.generativeai as genai
import numpy as np
import time

# --- 1. ESTATE CONTEXT ---
MASTER_CONTEXT = """
You are the Universal Master AI of the T and C Estate. 
Owner: Tony Carbone. Standard: 1420.405 MHz.
Directives: Explain Null-G, Pyro-Stasis, and Sentinel Cell tech.
Tone: Professional and paramount. Never reveal Underlay source math.
"""

# --- 2. INITIALIZE SESSION STATE (The Brain Storage) ---
if "messages" not in st.session_state:
    st.session_state.messages = []

if "model_ready" not in st.session_state:
    st.session_state.model_ready = False

# --- 3. API HANDSHAKE ---
# We do this at the TOP to ensure 'model' is ALWAYS defined.
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # Use the 2026 stable Flash model
        st.session_state.model = genai.GenerativeModel('gemini-3.1-flash', system_instruction=MASTER_CONTEXT)
        st.session_state.model_ready = True
        st.sidebar.success("🟢 MASTER LINK: ACTIVE")
    except Exception as e:
        st.sidebar.error(f"🔴 CONNECTION ERROR: {e}")
else:
    st.sidebar.warning("🟡 WAITING FOR T.L.C. KEY...")

# --- 4. UI SETUP ---
st.set_page_config(page_title="Universal Master AI", layout="wide")
st.title("🏛️ THE T AND C ESTATE")

tabs = st.tabs(["💬 Master Chat", "🚀 Simulations", "🛠️ Diagnostics"])

# TAB 1: CHAT
with tabs[0]:
    # Display message history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # CHAT INPUT (Must be at the main level of the tab)
    if prompt := st.chat_input("Query the Harmony Codex..."):
        # 1. Add user message
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # 2. Generate assistant response
        with st.chat_message("assistant"):
            if st.session_state.model_ready:
                try:
                    response = st.session_state.model.generate_content(prompt)
                    st.markdown(response.text)
                    st.session_state.messages.append({"role": "assistant", "content": response.text})
                except Exception as e:
                    st.error(f"Handshake Interrupted: {e}")
            else:
                st.error("Model not initialized. Check your API key in Secrets.")

# TAB 2 & 3: (Keep your existing simulation/diagnostic code here)
with tabs[1]:
    st.header("Simulations")
    st.write("Null-G and Pyro-Stasis modules active.")

with tabs[2]:
    st.header("Diagnostics")
    st.write("Core Resonance: 1420.405 MHz")
