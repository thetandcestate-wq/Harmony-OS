import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time

# --- 1. HARMONY OS CONTEXT ---
MASTER_CONTEXT = """
You are Harmony AI of Harmony OS. Owner: Tony Carbone. 
Standard: 1420.405 MHz. Directives: Professional, paramount.
"""

# --- 2. UI SETUP & FLOATING STYLE ---
st.set_page_config(page_title="Harmony OS", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050a0f; color: #00ffcc; }
    div[data-testid="stVerticalBlock"] > div:has(div.floating-anchor) {
        position: fixed; bottom: 30px; right: 30px; z-index: 999;
        background-color: #0a1520; padding: 10px; border: 1px solid #00ffcc;
        border-radius: 10px; box-shadow: 0 0 15px #00ffcc;
    }
    .main .block-container { padding-bottom: 180px; }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
if "ai_on" not in st.session_state:
    st.session_state.ai_on = False

# --- 3. SIDEBAR: VAULT MANAGEMENT ---
with st.sidebar:
    st.title("🏛️ VAULT MGMT")
    st.write("---")
    
    # OPTION 1: DELETE ENTIRE CHAT
    if st.button("🗑️ PURGE ENTIRE VAULT"):
        st.session_state.messages = []
        st.success("Vault Purged.")
        st.rerun()
    
    st.write("---")
    
    # OPTION 2: SELECT INDIVIDUAL TO DELETE
    if st.session_state.messages:
        st.subheader("Selective Deletion")
        # Create a list of user queries for the selection box
        options = [f"{i}: {m['content'][:30]}..." for i, m in enumerate(st.session_state.messages) if m['role'] == 'user']
        to_delete = st.multiselect("Select queries to remove:", options)
        
        if st.button("Remove Selected"):
            # Get the indices from the selected strings
            indices_to_remove = [int(s.split(":")[0]) for s in to_delete]
            # We remove both the user message and the subsequent assistant response
            # We iterate backwards to avoid index shifting issues
            for index in sorted(indices_to_remove, reverse=True):
                # Remove assistant response first (index + 1) then user message (index)
                if index + 1 < len(st.session_state.messages):
                    st.session_state.messages.pop(index + 1)
                st.session_state.messages.pop(index)
            st.rerun()
    else:
        st.info("Vault is currently empty.")

# --- 4. FLOATING TOGGLE ---
st.markdown('<div class="floating-anchor"></div>', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌ CLOSE AI"):
    st.session_state.ai_on = not st.session_state.ai_on
    st.rerun()

# --- 5. API HANDSHAKE & LAB ---
if "GEMINI_API_KEY" in st.secrets:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    MODEL_ID = "gemini-3.1-flash-lite-preview"
else:
    st.error("🔑 Key Missing")
    st.stop()

st.title("🏛️ THE T AND C ESTATE")
tab1, tab2 = st.tabs(["🚀 Null-G Simulation", "🛠️ System Diagnostics"])
with tab1:
    m_in = st.number_input("Mass (kg)", value=50000)
    if st.button("EXECUTE"): st.metric("Effective Mass", f"{m_in * 1e-8:.8f} kg")
with tab2:
    st.line_chart(1420.405 + 0.005 * np.sin(np.linspace(0, 10, 100)))

# --- 6. CHAT INTERFACE ---
if st.session_state.ai_on:
    st.divider()
    chat_box = st.container()
    for msg in st.session_state.messages:
        with chat_box.chat_message(msg["role"]): st.markdown(msg["content"])

    if prompt := st.chat_input("Query Harmony AI..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_box.chat_message("assistant"):
            response = client.models.generate_content(
                model=MODEL_ID, contents=prompt,
                config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT)
            )
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        st.rerun()
