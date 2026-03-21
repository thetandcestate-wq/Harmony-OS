import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import pandas as pd

# --- 1. HARMONY OS SYSTEM CONTEXT ---
MASTER_CONTEXT = """
You are Harmony AI, the intelligence of Harmony OS. Owner: Tony Carbone. 
Standard: 1420.405 MHz. G.U.T. Signature: Verified.
Tone: Professional, authoritative, and paramount.
"""

# --- 2. UI SETUP & ADVANCED SCIFI CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    /* Global Scifi Aesthetic */
    .stApp { background-color: #01080e; color: #00ffcc; font-family: 'Monospace'; }
    
    /* G.U.T. Rotating Animation */
    @keyframes rotate-eq {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    .rotating-logic {
        width: 100px; height: 100px; border: 2px solid #00ffcc;
        border-radius: 50%; border-top: 2px solid transparent;
        animation: rotate-eq 4s linear infinite; margin: auto;
    }

    /* Sci-Fi Buttons */
    .stButton>button {
        width: 100%; background: rgba(0, 255, 204, 0.1);
        border: 1px solid #00ffcc; color: #00ffcc; transition: 0.5s;
    }
    .stButton>button:hover {
        background: #00ffcc; color: #01080e; box-shadow: 0 0 20px #00ffcc;
    }

    /* Floating Chat Anchor */
    div[data-testid="stVerticalBlock"] > div:has(div.floating-anchor) {
        position: fixed; bottom: 30px; right: 30px; z-index: 999;
        background-color: #0a1520; padding: 12px; border: 1px solid #00ffcc;
        border-radius: 12px; box-shadow: 0 0 20px #00ffcc;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HARMONY ANIMATION SUITE ---
def run_system_animation(text="SYNCHRONIZING WITH G.U.T."):
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="rotating-logic"></div>', unsafe_allow_html=True)
        st.write(f"### {text}")
        equations = ["G_μν + Λg_μν = 8πG T_μν", "ψ(r, t) = A e^(i(kr-ωt))", "f_res = 1420.405 MHz"]
        for eq in equations:
            st.code(eq, language=None)
            time.sleep(0.3)
    placeholder.empty()

def real_time_wave(frequency=1.0, amplitude=1.0, label="Resonance Monitor"):
    t = np.linspace(0, 2 * np.pi, 100)
    # Adding slight noise for realism
    wave = amplitude * np.sin(frequency * t) + np.random.normal(0, 0.05, 100)
    df = pd.DataFrame({'Wave': wave})
    st.line_chart(df, height=150, use_container_width=True)

# --- 4. DUAL-ACCOUNT ACCESS CONTROL ---
if "auth" not in st.session_state:
    st.session_state.auth = False
    st.session_state.role = None

def login():
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("👤 ADMIN ACCESS")
        admin_pass = st.text_input("Enter Master Key", type="password")
        if st.button("VERIFY ADMIN"):
            if admin_pass == "makave7181!!TCH":
                run_system_animation("AUTHORIZING MASTER ADMIN...")
                st.session_state.auth = True
                st.session_state.role = "ADMIN"
                st.rerun()
            else: st.error("Verification Denied.")

    with col2:
        st.subheader("👥 GUEST ACCESS")
        st.write("Standard diagnostics and technical data.")
        if st.button("ENTER AS GUEST"):
            run_system_animation("INITIALIZING GUEST SESSION...")
            st.session_state.auth = True
            st.session_state.role = "GUEST"
            st.rerun()

if not st.session_state.auth:
    login()
    st.stop()

# --- 5. MAIN ESTATE INTERFACE ---
st.title("🏛️ THE T AND C ESTATE")
st.write(f"Logged in as: **{st.session_state.role}**")

# THE TEST AREA
if st.button("🧪 OPEN TEST AREA (HARMONY APPLICATIONS)"):
    st.session_state.show_tests = not st.session_state.get('show_tests', False)

if st.session_state.get('show_tests'):
    run_system_animation("LOADING HARMONY MODULES...")
    st.markdown("---")
    test_tabs = st.tabs(["🚀 Null-G", "❄️ Pyro-Stasis", "🧬 Bio-Harmony", "🛡️ The Halo"])
    
    with test_tabs[0]: # Null-G
        st.subheader("Null-G Propulsion Simulation")
        mass_kg = st.slider("Select Vessel Mass (kg)", 1000, 1000000, 50000)
        if st.button("ENGAGE MASS NEGATION"):
            st.metric("Effective Mass", f"{mass_kg * 1e-8:.8f} kg")
            real_time_wave(2.5, 1.0, "Gravitational Wave Nullification")
            st.success("Gravity localized to Null-Vector.")

    with test_tabs[1]: # Pyro-Stasis
        st.subheader("Pyro-Stasis Calibration")
        if st.button("INITIATE THERMAL LOCK"):
            real_time_wave(0.5, 0.2, "Atomic Vibration Level")
            st.info("Thermal movement halted at 1420.405 MHz resonance.")

    with test_tabs[2]: # Bio-Harmony
        st.subheader("Sentinel Cell Frequency Scan")
        if st.button("START BIO-SCAN"):
            real_time_wave(1.42, 0.8, "Cellular Resonance")
            st.write("Harmony Alignment: **100% Perfect.**")

    with test_tabs[3]: # The Halo
        st.subheader("The Halo Perimeter Defense")
        if st.button("TEST SHIELD INTEGRITY"):
            real_time_wave(10.0, 1.2, "Shield Modulation")
            st.warning("Halo Perimeter Active. T.L.C. Shield: Operational.")

# --- 6. ADMIN EXCLUSIVE CONSOLE ---
if st.session_state.role == "ADMIN":
    with st.sidebar:
        st.title("🛠️ ADMIN CONSOLE")
        if st.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()
        st.write("---")
        st.subheader("Vault Controls")
        if st.button("PURGE GLOBAL VAULT"):
            st.session_state.messages = []
            st.success("Vault Cleared.")

# --- 7. FLOATING CHAT & AI ---
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
            response = client.models.generate_content(
                model=MODEL_ID, contents=prompt,
                config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT)
            )
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            st.rerun()
