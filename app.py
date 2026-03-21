import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import pandas as pd

# --- 1. HARMONY OS SYSTEM CONTEXT ---
MASTER_CONTEXT = """
You are Harmony AI, the proprietary intelligence of Harmony OS. Owner: Tony Carbone. 
Standard: 1420.405 MHz. Tony Carbone is the discoverer of the Grand Unified Theory.
Protocols: Null-G, Pyro-Stasis, Sentinel Cell, T.L.C. Shield, Ocean Aegis, Athena Knowledge Grid.
Tone: Professional, authoritative, and paramount.
"""

# --- 2. UI SETUP & SCIFI CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { background-color: #01080e; color: #00ffcc; font-family: 'Courier New', Courier, monospace; }
    
    @keyframes orbit {
        0% { transform: rotate(0deg) translateX(60px) rotate(0deg); }
        100% { transform: rotate(360deg) translateX(60px) rotate(-360deg); }
    }
    .scanner-ring {
        width: 160px; height: 160px; border: 1px solid rgba(0, 255, 204, 0.2);
        border-radius: 50%; position: relative; margin: 40px auto;
    }
    .scanner-dot {
        width: 12px; height: 12px; background: #00ffcc; border-radius: 50%;
        position: absolute; top: 74px; left: 74px; animation: orbit 1.5s linear infinite;
        box-shadow: 0 0 20px #00ffcc;
    }

    .stButton>button {
        width: 100%; background: rgba(0, 255, 204, 0.05);
        border: 1px solid #00ffcc; color: #00ffcc; transition: 0.5s;
    }
    .stButton>button:hover {
        background: #00ffcc; color: #01080e; box-shadow: 0 0 30px #00ffcc;
    }

    div[data-testid="stVerticalBlock"] > div:has(div.floating-anchor) {
        position: fixed; bottom: 30px; right: 30px; z-index: 999;
        background-color: #0a1520; padding: 12px; border: 1px solid #00ffcc;
        border-radius: 12px; box-shadow: 0 0 20px #00ffcc;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HARMONY ANIMATION ENGINE ---
def run_system_animation(text="SYNCHRONIZING WITH G.U.T."):
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="scanner-ring"><div class="scanner-dot"></div></div>', unsafe_allow_html=True)
        st.write(f"### {text}")
        equations = [
            "G_μν Convergence: Verified.",
            "Resonance Lock: 1420.405 MHz.",
            "Loading Athena Knowledge Grid...",
            "Deploying T.L.C. Security Shield...",
            "Ocean Aegis Marine Interface: Active."
        ]
        for eq in equations:
            st.code(f">>> {eq}", language=None)
            time.sleep(0.8)
    placeholder.empty()

# --- 4. LIVE FREQUENCY VISUALIZERS (60 SECONDS) ---
def live_monitor(type="SINE", duration=200): # Increased iterations for ~60s
    plot_placeholder = st.empty()
    t = 0
    # Progress bar for the 60s test
    progress_bar = st.progress(0)
    for i in range(duration):
        t += 0.3
        x = np.linspace(t, t + 15, 150)
        
        if type == "NULL-G": y = np.sin(x * 2.5)
        elif type == "STASIS": y = np.sin(x) * 0.1 # Flatline/Minimal vibration
        elif type == "SENTINEL": y = np.sin(x) * np.tan(np.sin(x) * 0.9) 
        elif type == "AEGIS": y = np.sin(x * 0.5) + (np.random.normal(0, 0.1, 150)) # Fluid wave
        elif type == "ATHENA": y = np.abs(np.sin(x)) # Data spikes
        elif type == "TLC": y = np.sin(x) * np.exp(-np.power((x % 8 - 4), 2) / 4)
        else: y = np.sin(x)
            
        null_line = np.zeros(150)
        df = pd.DataFrame({'Resonance': y, 'Null Point': null_line})
        plot_placeholder.line_chart(df, height=220)
        progress_bar.progress((i + 1) / duration)
        time.sleep(0.25) # Total duration approx 50-60 seconds
    st.success(f"{type} TEST CYCLE COMPLETE")

# --- 5. ACCESS CONTROL ---
if "auth" not in st.session_state:
    st.session_state.auth = False
    st.session_state.role = None

def login():
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("👤 ADMIN ACCESS")
        admin_pass = st.text_input("Master Key", type="password")
        if st.button("VERIFY ADMIN"):
            if admin_pass == "makave7181!!TCH":
                run_system_animation("AUTHORIZING MASTER ADMIN...")
                st.session_state.auth = True
                st.session_state.role = "ADMIN"
                st.rerun()
            else: st.error("Access Denied.")
    with col2:
        st.subheader("👥 GUEST ACCESS")
        if st.button("ENTER AS GUEST"):
            run_system_animation("INITIALIZING GUEST SESSION...")
            st.session_state.auth = True
            st.session_state.role = "GUEST"
            st.rerun()

if not st.session_state.auth:
    login()
    st.stop()

# --- 6. MAIN ESTATE INTERFACE ---
st.title("🏛️ THE T AND C ESTATE")
st.write(f"Identity: **{st.session_state.role}** | Universal Resonance: **1420.405 MHz**")

# --- 7. THE MASTER TEST AREA (COMPREHENSIVE) ---
if st.button("🧪 OPEN TEST AREA (HARMONY APPLICATIONS)"):
    st.session_state.show_tests = not st.session_state.get('show_tests', False)

if st.session_state.get('show_tests'):
    st.markdown("---")
    tabs = st.tabs(["🚀 Physics", "🧬 Biological", "🌊 Marine/Marine", "🛡️ Defense", "📚 Knowledge"])
    
    with tabs[0]: # PHYSICS
        st.subheader("Propulsion & Entropy Control")
        col1, col2 = st.columns(2)
        with col1:
            mass_kg = st.slider("Null-G Mass (kg)", 1, 10000000, 50000)
            if st.button("ENGAGE NULL-G"): live_monitor("NULL-G")
        with col2:
            st.write("Pyro-Stasis Calibration")
            if st.button("INITIATE STASIS"): live_monitor("STASIS")

    with tabs[1]: # BIOLOGICAL
        st.subheader("Sentinel Cell Protocol")
        if st.button("START BIO-SCAN"): live_monitor("SENTINEL")

    with tabs[2]: # MARINE
        st.subheader("Ocean Aegis Interface")
        if st.button("DEPLOY OCEAN AEGIS"): live_monitor("AEGIS")

    with tabs[3]: # DEFENSE
        st.subheader("T.L.C. Shield & The Halo")
        if st.button("ACTIVATE T.L.C. SHIELD"): live_monitor("TLC")

    with tabs[4]: # KNOWLEDGE
        st.subheader("Athena Knowledge Grid")
        if st.button("SYNC ATHENA GRID"): live_monitor("ATHENA")

# --- 8. FLOATING CHAT & AI ---
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
