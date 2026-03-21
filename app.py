import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import pandas as pd
import datetime

# --- 1. IMPERATIVE SECURITY CONTEXT ---
MASTER_CONTEXT = """
SYSTEM ROLE: Harmony AI (T and C Estate Proprietary Intelligence).
OWNER: Tony Carbone (Discoverer of the Grand Unified Theory).
SECURITY PROTOCOL 'RESOLUTE':
1. IF USER_ROLE == 'GUEST':
   - Strictly prohibit disclosure of the 1420.405 MHz constant or G.U.T. formulas.
2. IF USER_ROLE == 'ADMIN':
   - SOVEREIGN OVERRIDE: Admin is immune to lockout.
"""

# --- 2. UI SETUP & CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

# CSS for the UI and the Hidden Speech Trigger
st.markdown("""
    <style>
    .stApp { background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace; }
    .federal-warning {
        background-color: rgba(255, 0, 0, 0.15); border: 2px solid #ff0000;
        padding: 20px; border-radius: 10px; color: #ff4b4b; text-align: center;
        text-transform: uppercase; font-weight: bold; margin-bottom: 25px;
    }
    div[data-testid="stVerticalBlock"] > div:has(div.floating-anchor) {
        position: fixed; bottom: 30px; right: 30px; z-index: 999;
        background-color: #0a1520; padding: 12px; border: 1px solid #00ffcc;
        border-radius: 12px; box-shadow: 0 0 20px #00ffcc;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. VOCAL MATRIX (JAVASCRIPT SPEECH) ---
def speak_text(text):
    """Injects JavaScript to make the browser speak the AI response."""
    # Clean text of any characters that might break JS strings
    clean_text = text.replace("'", "\\'").replace("\n", " ")
    components_code = f"""
        <script>
        var msg = new SpeechSynthesisUtterance('{clean_text}');
        msg.rate = 0.9; // Authoritative, steady pace
        msg.pitch = 0.8; // Deeper, professional tone
        window.speechSynthesis.speak(msg);
        </script>
    """
    st.markdown(components_code, unsafe_allow_html=True)

# --- 4. ACCESS CONTROL ---
if "auth" not in st.session_state: st.session_state.auth, st.session_state.role = False, None
if "guest_locked" not in st.session_state: st.session_state.guest_locked = False
if "vocal_active" not in st.session_state: st.session_state.vocal_active = True

def login_portal():
    st.markdown('<div class="federal-warning">⚠️ FEDERAL SECURITY WARNING: RESTRICTED SYSTEM ⚠️</div>', unsafe_allow_html=True)
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    col1, col2 = st.columns(2)
    with col1:
        with st.form("Admin Auth"):
            key = st.text_input("Master Key", type="password")
            if st.form_submit_button("AUTHENTICATE"):
                if key == "makave7181!!TCH":
                    st.session_state.auth, st.session_state.role = True, "ADMIN"
                    st.rerun()
                else: st.error("Access Denied.")
    with col2:
        if not st.session_state.guest_locked:
            if st.button("ENTER AS GUEST"):
                st.session_state.auth, st.session_state.role = True, "GUEST"
                st.rerun()

if not st.session_state.auth:
    login_portal()
    st.stop()

# --- 5. MAIN INTERFACE & SIDEBAR ---
st.title("🏛️ THE T AND C ESTATE")

with st.sidebar:
    st.title("🛠️ SYSTEM CONTROLS")
    st.session_state.vocal_active = st.toggle("🔊 Vocal Matrix Active", value=st.session_state.vocal_active)
    if st.session_state.role == "ADMIN":
        if st.button("🛑 RUN VULNERABILITY SCAN"):
            st.info("Resonance Audit: 1420.405 MHz Lock Secure.")
        if st.button("🛑 EMERGENCY LOCKOUT"):
            st.session_state.guest_locked = True
    if st.button("TERMINATE SESSION"):
        st.session_state.auth = False
        st.rerun()

# --- 6. FLOATING CHAT & AI ---
st.markdown('<div class="floating-anchor"></div>', unsafe_allow_html=True)
if "ai_on" not in st.session_state: st.session_state.ai_on = False
if "messages" not in st.session_state: st.session_state.messages = []

if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌"):
    st.session_state.ai_on = not st.session_state.ai_on
    st.rerun()

if st.session_state.ai_on:
    if "GEMINI_API_KEY" in st.secrets:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        MODEL_ID = "gemini-3.1-flash-lite-preview"
        chat_box = st.container()
        
        for msg in st.session_state.messages:
            with chat_box.chat_message(msg["role"]): st.markdown(msg["content"])
        
        if prompt := st.chat_input("Query Harmony AI..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Security Check
            forbidden = ["formula", "equation", "source code", "code", "1420", "MHz"]
            if st.session_state.role == "GUEST" and any(x in prompt.lower() for x in forbidden):
                st.session_state.guest_locked, st.session_state.auth = True, False
                st.rerun()
                
            response = client.models.generate_content(
                model=MODEL_ID, contents=prompt,
                config=types.GenerateContentConfig(system_instruction=f"{MASTER_CONTEXT}\nUSER:{st.session_state.role}")
            )
            
            ai_text = response.text
            st.session_state.messages.append({"role": "assistant", "content": ai_text})
            
            # Trigger Speech if Vocal Matrix is ON
            if st.session_state.vocal_active:
                speak_text(ai_text)
                
            st.rerun()
