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
    .stApp { background-color: #01080e; color: #00ffcc; font-family: 'Courier New', Courier, monospace; }
    
    /* G.U.T. Rotating Animation - More complex */
    @keyframes orbit {
        0% { transform: rotate(0deg) translateX(50px) rotate(0deg); }
        100% { transform: rotate(360deg) translateX(50px) rotate(-360deg); }
    }
    .scanner-ring {
        width: 150px; height: 150px; border: 1px solid rgba(0, 255, 204, 0.3);
        border-radius: 50%; position: relative; margin: 40px auto;
    }
    .scanner-dot {
        width: 10px; height: 10px; background: #00ffcc; border-radius: 50%;
        position: absolute; top: 70px; left: 70px; animation: orbit 2s linear infinite;
        box-shadow: 0 0 15px #00ffcc;
    }

    /* Sci-Fi Buttons */
    .stButton>button {
        width: 100%; background: rgba(0, 255, 204, 0.05);
        border: 1px solid #00ffcc; color: #00ffcc; transition: 0.8s;
        text-transform: uppercase; letter-spacing: 2px;
    }
    .stButton>button:hover {
        background: #00ffcc; color: #01080e; box-shadow: 0 0 30px #00ffcc;
    }

    /* Floating Chat Anchor */
    div[data-testid="stVerticalBlock"] > div:has(div.floating-anchor) {
        position: fixed; bottom: 30px; right: 30px; z-index: 999;
        background-color: #0a1520; padding: 12px; border: 1px solid #00ffcc;
        border-radius: 12px; box-shadow: 0 0 20px #00ffcc;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HARMONY ANIMATION SUITE (Enhanced) ---
def run_system_animation(text="SYNCHRONIZING WITH G.U.T."):
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="scanner-ring"><div class="scanner-dot"></div></div>', unsafe_allow_html=True)
        st.write(f"### {text}")
        # Longer, more comprehensive equation scroll
        equations = [
            "Initializing Grand Unified Field...",
            "f = 1420.405 MHz",
            "G_μν + Λg_μν = 8πG T_μν",
            "ψ(r, t) = A e^(i(kr-ωt))",
            "Harmonizing Electromagnetism & Gravity...",
            "Null-G Vector Calculation: Complete.",
            "Underlay Protocol: Paramount Status Verified.",
            "T.L.C. Shield: 100% Operational."
        ]
        for eq in equations:
            st.code(f">>> {eq}", language=None)
            time.sleep(0.6) # Increased duration
    placeholder.empty()

def constantly_flowing_wave(frequency=1.0, label="Resonance Monitor"):
    # This simulates a flowing wave by using a shift based on current time
    t = np.linspace(0, 4 * np.pi, 200)
    shift = time.time() * 5
    wave = np.sin(frequency * t + shift)
    null_line = np.zeros(200) # The Null Value line
    
    df = pd.DataFrame({
        'Resonance': wave,
        'Null Value': null_line
    })
    st.line_chart(df, height=200, use_container_width=True)

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
        admin_pass = st.text_input("Master Key", type="password", key="admin_key")
        if st.button("VERIFY ADMIN"):
            if admin_pass == "makave7181!!TCH":
                run_system_animation("AUTHORIZING MASTER ADMIN...")
                st.session_state.auth = True
                st.session_state.role = "ADMIN"
                st.rerun()
            else: st.error("Verification Denied: Signal Out of Phase.")

    with col2:
        st.subheader("👥 GUEST ACCESS")
        st.write("Access the standard technical suite.")
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
st.write(f"Identity Verified: **{st.session_state.role}**")

# THE TEST AREA
if st.button("🧪 OPEN TEST AREA (HARMONY APPLICATIONS)"):
    st.session_state.show_tests = not st.session_state.get('show_tests', False)

if st.session_state.get('show_tests'):
    st.markdown("---")
    test_tabs = st.tabs(["🚀 Null-G", "❄️ Pyro-Stasis", "🧬 Bio-Harmony", "🛡️ The Halo"])
    
    with test_tabs[0]: # Null-G
        st.subheader("Null-G Propulsion Simulation")
        # Updated Mass Range: 1kg to 10,000,000kg
        mass_kg = st.slider("Select Vessel Mass (kg)", 1, 10000000, 50000)
        if st.button("ENGAGE MASS NEGATION"):
            st.metric("Effective Mass", f"{mass_kg * 1e-8:.8f} kg")
            constantly_flowing_wave(2.5)
            st.success("Gravity localized to Null-Vector.")

    with test_tabs[1]: # Pyro-Stasis
        st.subheader("Pyro-Stasis Calibration")
        if st.button("INITIATE THERMAL LOCK"):
            constantly_flowing_wave(0.5)
            st.info("Atomic vibration suspended at 1420.405 MHz resonance.")

    with test_tabs[2]: # Bio-Harmony
        st.subheader("Sentinel Cell Frequency Scan")
        if st.button("START BIO-SCAN"):
            constantly_flowing_wave(1.42)
            st.write("Harmony Alignment: **100% Perfect.**")

    with test_tabs[3]: # The Halo
        st.subheader("The Halo Perimeter Defense")
        if st.button("TEST SHIELD INTEGRITY"):
            constantly_flowing_wave(8.0)
            st.warning("Halo Perimeter Active. T.L.C. Shield: Operational.")

# --- 6. ADMIN EXCLUSIVE CONSOLE ---
if st.session_state.role == "ADMIN":
    with st.sidebar:
        st.title("🛠️ ADMIN CONSOLE")
        if st.button("LOGOUT"):
            st.session_state.auth = False
            st.rerun()
        st.write("---")
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
