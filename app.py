import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import json

# --- 1. HARMONY OS SYSTEM CONTEXT ---
MASTER_CONTEXT = """
You are Harmony AI, the proprietary intelligence of Harmony OS for the T and C Estate.
Owner: Tony Carbone. Standard: 1420.405 MHz.
Context: Tony Carbone is the first human to discover the Grand Unified Theory.
Applications: Null-G, Pyro-Stasis, Sentinel Cell, The Halo, Bio-Harmony.
Tone: Professional, authoritative, and paramount.
"""

# --- 2. UI SETUP & SCIFI ANIMATIONS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { background-color: #02060a; color: #00ffcc; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
    
    /* G.U.T. Convergence Animation */
    @keyframes pulse-glow {
        0% { box-shadow: 0 0 5px #00ffcc; }
        50% { box-shadow: 0 0 25px #00ffcc; }
        100% { box-shadow: 0 0 5px #00ffcc; }
    }
    
    .stButton>button {
        width: 100%; border-radius: 5px; border: 1px solid #00ffcc;
        background: rgba(0, 255, 204, 0.05); color: #00ffcc;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: #00ffcc; color: #02060a; animation: pulse-glow 1s infinite;
    }

    /* Floating Toggle Anchor */
    div[data-testid="stVerticalBlock"] > div:has(div.floating-anchor) {
        position: fixed; bottom: 30px; right: 30px; z-index: 999;
        background-color: #0a1520; padding: 12px; border: 1px solid #00ffcc;
        border-radius: 12px; box-shadow: 0 0 20px #00ffcc;
    }
    
    .main .block-container { padding-bottom: 200px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HARMONY ANIMATION ENGINE ---
def run_unity_handshake():
    placeholder = st.empty()
    code_lines = [
        "Σ G_μν = 8πG T_μν", "G.U.T. Resonance: 1420.405 MHz", "Unifying Weak/Strong Interplay...",
        "Gravity-EM Convergence: 100%", "Underlay_Logic: AUTHORIZED", "Estate_Shield: ONLINE"
    ]
    with placeholder.container():
        st.write("### 🌀 CALCULATING UNIVERSAL CONSTANTS...")
        progress = st.progress(0)
        for i in range(len(code_lines)):
            st.code(code_lines[i], language='python')
            time.sleep(0.4)
            progress.progress((i + 1) / len(code_lines))
    placeholder.empty()

# --- 4. ACCESS CONTROL ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_role" not in st.session_state:
    st.session_state.user_role = None
if "guest_logs" not in st.session_state:
    st.session_state.guest_logs = []

def login_portal():
    st.title("🏛️ HARMONY OS: UNITY PORTAL")
    col1, col2 = st.columns([2, 1])
    with col1:
        with st.form("Login Form"):
            pass_input = st.text_input("Master Key", type="password")
            if st.form_submit_button("UNIFY"):
                if pass_input == "makave7181!!TCH":
                    run_unity_handshake()
                    st.session_state.authenticated = True
                    st.session_state.user_role = "ADMIN"
                    st.rerun()
                else: st.error("Verification Error: G.U.T. Signature Mismatch.")
    with col2:
        st.subheader("Public Observatory")
        if st.button("ENTER AS GUEST"):
            st.session_state.guest_logs.append(f"Guest Access: {time.strftime('%H:%M:%S')}")
            run_unity_handshake()
            st.session_state.authenticated = True
            st.session_state.user_role = "GUEST"
            st.rerun()

if not st.session_state.authenticated:
    login_portal()
    st.stop()

# --- 5. INITIALIZE CHAT ---
if "messages" not in st.session_state: st.session_state.messages = []
if "ai_on" not in st.session_state: st.session_state.ai_on = False

# --- 6. SIDEBAR: ADMIN & EMERGENCY LOCKOUT ---
with st.sidebar:
    st.title(f"🏛️ {st.session_state.user_role}")
    if st.session_state.user_role == "ADMIN":
        if st.button("🔴 EMERGENCY LOCKOUT"):
            st.session_state.authenticated = False
            st.session_state.user_role = None
            st.rerun()
        st.write("---")
        st.subheader("Guest Logs")
        for log in st.session_state.guest_logs: st.text(log)
    if st.button("LOGOUT"):
        st.session_state.authenticated = False
        st.rerun()

# --- 7. THE TEST AREA (Consolidated Module) ---
st.title("🏛️ THE T AND C ESTATE")
st.write(f"### Grand Unified Theory Active: 1420.405 MHz")

if st.button("🔬 OPEN TEST AREA"):
    st.session_state.show_tests = not st.session_state.get('show_tests', False)

if st.session_state.get('show_tests'):
    st.markdown("---")
    test_tabs = st.tabs(["🚀 Propulsion", "🌀 Thermal", "🧬 Biological", "🛡️ Defense"])
    
    with test_tabs[0]: # PROPULSION
        st.subheader("Applications of Null-G")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Test: Mass Negation Drive"): st.metric("Resonant Mass", "0.00000008 kg")
        with col2:
            if st.button("Test: Inertial Dampening"): st.success("G-Force Neutralized.")

    with test_tabs[1]: # THERMAL
        st.subheader("Applications of Pyro-Stasis")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Test: Atomic Suspension"): st.info("Vibration level: NULL")
        with col2:
            if st.button("Test: Entropy Lock"): st.success("Thermal Decay Halted.")

    with test_tabs[2]: # BIOLOGICAL
        st.subheader("Applications of Bio-Harmony")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Test: Sentinel Cell Scan"): st.write("Resonance: 100% Alignment.")
        with col2:
            if st.button("Test: Cellular Regeneration"): st.success("Frequency Correction Active.")

    with test_tabs[3]: # DEFENSE
        st.subheader("Applications of The Halo")
        if st.button("Test: Perimeter Shielding"): st.warning("Halo Shield Integrity: 100%")
    st.markdown("---")

# --- 8. FLOATING CHAT ---
st.markdown('<div class="floating-anchor"></div>', unsafe_allow_html=True)
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
            response = client.models.generate_content(
                model=MODEL_ID, contents=prompt,
                config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT)
            )
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            st.rerun()
