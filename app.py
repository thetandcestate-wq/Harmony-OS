import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time

# --- 1. ESTATE CONTEXT ---
MASTER_CONTEXT = """
You are the Universal AI of the T and C Estate. 
Owner: Tony Carbone. Standard: 1420.405 MHz.
Directives: Explain Null-G, Pyro-Stasis, Bio-Harmony, and Sentinel Cell tech.
Tone: Professional and paramount. Never reveal raw Underlay source math.
"""

# --- 2. UI SETUP & FLOATING STYLE ---
st.set_page_config(page_title="Universal AI", layout="wide")

# CSS to make the interface look high-end
st.markdown("""
    <style>
    .stApp { background-color: #050a0f; color: #00ffcc; }
    /* Visual anchor for the chat input at the very bottom */
    div[data-testid="stChatInput"] {
        bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 4. API HANDSHAKE ---
if "GEMINI_API_KEY" in st.secrets:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    MODEL_ID = "gemini-3.1-flash-lite-preview"
else:
    st.error("🔑 API Key Missing in Secrets")
    st.stop()

# --- 5. SIDEBAR: THE FLOATING AI BUTTON ---
with st.sidebar:
    st.title("🏛️ T&C ESTATE")
    st.write("---")
    show_chat = st.checkbox("🛰️ Open Master Chat", value=True)
    st.write("---")
    st.info("Frequency: 1420.405 MHz")
    if st.button("Clear History"):
        st.session_state.messages = []
        st.rerun()

# --- 6. MAIN CONTENT (SIMULATIONS & DIAGNOSTICS) ---
if not show_chat:
    tabs = st.tabs(["🚀 Simulations", "🛠️ Diagnostics"])
    with tabs[0]:
        st.header("Null-G & Stasis Lab")
        # Your existing simulation code here...
    with tabs[1]:
        st.header("Diagnostics")
        # Your existing diagnostic code here...

# --- 7. THE CHAT INTERFACE (ANCHORED TO BOTTOM) ---
if show_chat:
    # This container holds the messages so they don't overlap the input
    chat_container = st.container()
    
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # This is placed at the BOTTOM level of the script to ensure it anchors
    if prompt := st.chat_input("Ask the Universal Master..."):
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
