import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import pandas as pd
import random
import datetime
import streamlit.components.v1 as components

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

st.markdown("""
    <style>
    .stApp { background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace; }
    
    /* Federal Warning */
    .federal-warning {
        background-color: rgba(255, 0, 0, 0.15); border: 2px solid #ff0000;
        padding: 20px; border-radius: 10px; color: #ff4b4b; text-align: center;
        text-transform: uppercase; font-weight: bold; margin-bottom: 25px;
    }

    /* Interactive Test Cards */
    .test-card {
        border: 1px solid #00ffcc; padding: 20px; border-radius: 12px;
        background: rgba(0, 255, 204, 0.05); transition: 0.4s ease;
        margin-bottom: 10px;
    }
    .test-card:hover { background: rgba(0, 255, 204, 0.15); box-shadow: 0 0 25px #00ffcc; }

    /* Warp Effect */
    @keyframes warp-pulse {
        0% { transform: translate(-50%, -50%) scale(0.8); opacity: 0; }
        100% { transform: translate(-50%, -50%) scale(2.5); opacity: 0; }
    }
    .warp-effect {
        position: fixed; top: 50%; left: 50%; width: 400px; height: 400px;
        border: 1px solid #00ffcc; border-radius: 50%;
        animation: warp-pulse 1.2s ease-out infinite; pointer-events: none; z-index: 9999;
    }

    /* FLOATING ANCHOR FIX */
    .floating-anchor {
        position: fixed; bottom: 30px; right: 30px; z-index: 1000;
        background-color: #0a1520; padding: 15px; border: 1px solid #00ffcc;
        border-radius: 12px; box-shadow: 0 0 20px #00ffcc;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. VOCAL ENGINE (RE-BUILT FOR STREAMLIT) ---
def speak_response(text):
    """Injected via components to avoid UI blocking."""
    clean_text = text.replace("'", "\\'").replace("\n", " ")
    components.html(f"""
        <script>
        window.speechSynthesis.cancel();
        var msg = new SpeechSynthesisUtterance('{clean_text}');
        msg.rate = 0.9;
        msg.pitch = 0.8;
        window.speechSynthesis.speak(msg);
        </script>
    """, height=0)

# --- 4. SESSION STATE INITIALIZATION ---
if "auth" not in st.session_state: st.session_state.auth = False
if "role" not in st.session_state: st.session_state.role = None
if "guest_locked" not in st.session_state: st.session_state.guest_locked = False
if "vocal_active" not in st.session_state: st.session_state.vocal_active = True
if "ai_on" not in st.session_state: st.session_state.ai_on = False
if "messages" not in st.session_state: st.session_state.messages = []
if "archive_logs" not in st.session_state: st.session_state.archive_logs = []

# --- 5. LOGIN PORTAL ---
def login_portal():
    st.markdown('<div class="federal-warning">⚠️ FEDERAL SECURITY WARNING: RESTRICTED SYSTEM ⚠️</div>', unsafe_allow_html=True)
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    col1, col2 = st.columns(2)
    with col1:
        with st.form("Admin Auth"):
            key = st.text_input("Master Key", type="password")
            if st.form_submit_button("AUTHENTICATE"):
                if key == "makave7181!!TCH":
                    st.session_state.auth = True
                    st.session_state.role = "ADMIN"
                    st.rerun()
                else: st.error("Access Denied.")
    with col2:
        if not st.session_state.guest_locked:
            if st.button("ENTER AS GUEST"):
                st.session_state.auth = True
                st.session_state.role = "GUEST"
                st.rerun()
        else:
            st.warning("GUEST ACCESS SEVERED.")

if not st.session_state.auth:
    login_portal()
    st.stop()

# --- 6. SIDEBAR CONTROLS (VAULT & TERMINATE) ---
with st.sidebar:
    st.title("🏛️ ESTATE TOOLS")
    st.write(f"Identity: **{st.session_state.role}**")
    st.write("---")
    
    st.session_state.vocal_active = st.toggle("🔊 Vocal Matrix Active", value=st.session_state.vocal_active)
    
    if st.session_state.role == "ADMIN":
        st.subheader("📜 Estate Archive")
        if st.session_state.archive_logs:
            st.dataframe(pd.DataFrame(st.session_state.archive_logs))
            st.download_button("💾 DOWNLOAD VAULT", pd.DataFrame(st.session_state.archive_logs).to_csv(index=False), "vault.csv")
        
        if st.button("🛑 EMERGENCY GUEST LOCKOUT"):
            st.session_state.guest_locked = True
            st.success("Guest Access Blocked.")

    st.write("---")
    if st.button("🔚 TERMINATE SESSION"):
        st.session_state.auth = False
        st.session_state.role = None
        st.rerun()

# --- 7. MAIN INTERFACE & TEST AREA ---
st.title("🏛️ THE T AND C ESTATE")

if st.button("🧪 ACCESS HARMONY APPLICATIONS"):
    st.session_state.show_tests = not st.session_state.get('show_tests', False)

if st.session_state.get('show_tests'):
    tabs = st.tabs(["🚀 Physics", "🧬 Bio-Harmony", "🛡️ Defense"])
    with tabs[0]: 
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="test-card">', unsafe_allow_html=True)
            st.write("### Null-G Drive")
            mass = st.slider("Mass (kg)", 1, 10000000, 50000)
            if st.button("ENGAGE"): st.info(f"Engaging {mass}kg negation...")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="test-card">', unsafe_allow_html=True)
            st.write("### Pyro-Stasis")
            if st.button("LOCK ENTROPY"): st.info("Entropy suspension active.")
            st.markdown('</div>', unsafe_allow_html=True)

# --- 8. FLOATING AI TOGGLE & CHAT ---
# Pinned to bottom right
st.markdown('<div class="floating-anchor">', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌ CLOSE AI"):
    st.session_state.ai_on = not st.session_state.ai_on
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.ai_on:
    st.divider()
    if "GEMINI_API_KEY" in st.secrets:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        MODEL_ID = "gemini-3.1-flash-lite-preview"
        
        chat_container = st.container()
        for msg in st.session_state.messages:
            with chat_container.chat_message(msg["role"]): st.markdown(msg["content"])
        
        if prompt := st.chat_input("Query Harmony AI..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Security
            if st.session_state.role == "GUEST" and any(x in prompt.lower() for x in ["formula", "source code"]):
                st.session_state.guest_locked, st.session_state.auth = True, False
                st.rerun()
                
            response = client.models.generate_content(
                model=MODEL_ID, contents=prompt,
                config=types.GenerateContentConfig(system_instruction=f"{MASTER_CONTEXT}\nUSER:{st.session_state.role}")
            )
            
            ai_text = response.text
            st.session_state.messages.append({"role": "assistant", "content": ai_text})
            
            # SPEAK RESPONSE
            if st.session_state.vocal_active:
                speak_response(ai_text)
                
            st.rerun()
