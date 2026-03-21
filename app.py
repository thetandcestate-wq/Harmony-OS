import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import pandas as pd
import random

# --- 1. HARMONY OS SYSTEM CONTEXT ---
MASTER_CONTEXT = """
You are Harmony AI, the proprietary intelligence of Harmony OS. Owner: Tony Carbone. 
Standard: 1420.405 MHz. Tony Carbone is the discoverer of the Grand Unified Theory.
Protocols: Null-G, Pyro-Stasis, Sentinel Cell, T.L.C. Shield, Ocean Aegis, Athena Knowledge Grid.
Tone: Professional, authoritative, and paramount.
"""

# --- 2. UI SETUP & QUANTUM WARP CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace; }
    
    /* Warp Drive & Quantum Field Animations */
    @keyframes warp-speed {
        0% { transform: scale(1); opacity: 0.1; }
        50% { transform: scale(1.5); opacity: 0.5; }
        100% { transform: scale(2); opacity: 0; }
    }
    .warp-line {
        position: fixed; top: 50%; left: 50%; width: 2px; height: 100px;
        background: linear-gradient(to bottom, transparent, #00ffcc);
        animation: warp-speed 0.5s linear infinite;
    }
    
    @keyframes quantum-spin {
        from { transform: rotate(0deg) scale(1); }
        to { transform: rotate(360deg) scale(1.2); }
    }
    .quantum-core {
        width: 100px; height: 100px; border: 1px dashed #00ffcc;
        border-radius: 50%; animation: quantum-spin 2s linear infinite;
        margin: 20px auto; box-shadow: 0 0 20px #00ffcc;
    }

    /* Sci-Fi UI Elements */
    .stButton>button {
        width: 100%; background: rgba(0, 255, 204, 0.05);
        border: 1px solid #00ffcc; color: #00ffcc; transition: 0.3s;
        text-transform: uppercase;
    }
    .stButton>button:hover { background: #00ffcc; color: #01050a; box-shadow: 0 0 40px #00ffcc; }
    
    div[data-testid="stVerticalBlock"] > div:has(div.floating-anchor) {
        position: fixed; bottom: 30px; right: 30px; z-index: 999;
        background-color: #0a1520; padding: 12px; border: 1px solid #00ffcc;
        border-radius: 12px; box-shadow: 0 0 20px #00ffcc;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. RANDOMIZED SCIFI ANIMATION ENGINE ---
def run_quantum_transition(label="INITIALIZING PHASE SHIFT"):
    placeholder = st.empty()
    style = random.choice(["WARP", "QUANTUM", "TERMINAL"])
    
    with placeholder.container():
        if style == "WARP":
            st.markdown('<div class="warp-line" style="rotate: 45deg;"></div>', unsafe_allow_html=True)
            st.write(f"### 🌌 {label}: WARP ENGAGED")
        elif style == "QUANTUM":
            st.markdown('<div class="quantum-core"></div>', unsafe_allow_html=True)
            st.write(f"### ⚛️ {label}: QUANTUM LOCK")
        else:
            st.write(f"### 💾 {label}: EXECUTING G.U.T. LOGIC")
            
        logs = [
            "Collapsing Wave Functions...", "Stabilizing 1420.405 MHz Resonance...",
            "Expanding Event Horizon...", "Correcting Gravitational Entropy...",
            "Athena Grid Synchronizing...", "T.L.C. Security Verified."
        ]
        for log in random.sample(logs, 3):
            st.code(f">>> {log}")
            time.sleep(0.7)
    placeholder.empty()

# --- 4. REAL-TIME CORRECTION MONITOR (25 SECONDS) ---
def correction_monitor(tech_name, tech_type):
    run_quantum_transition(f"CALIBRATING {tech_name.upper()}")
    plot_placeholder = st.empty()
    status_placeholder = st.empty()
    t = 0
    duration = 100 # ~25s total
    
    for i in range(duration):
        t += 0.3
        x = np.linspace(t, t + 15, 150)
        ratio = i / duration
        noise = (1 - ratio) * np.random.normal(0, 1.8, 150)
        
        # Tech-specific wave signatures
        if tech_type == "NULL-G": base = np.sin(x * 3.0)
        elif tech_type == "STASIS": base = np.sin(x) * 0.02
        elif tech_type == "SENTINEL": base = np.sin(x) * np.tan(np.sin(x) * 0.85)
        elif tech_type == "TLC": base = np.sin(x) * np.exp(-np.power((x % 8 - 4), 2) / 4)
        else: base = np.sin(x)
            
        final_y = (base * ratio) + noise
        df = pd.DataFrame({'Harmony Resonance': final_y, 'Null Point': np.zeros(150)})
        plot_placeholder.line_chart(df, height=250)
        status_placeholder.write(f"**{tech_name}:** {int(ratio*100)}% Harmonic Alignment")
        time.sleep(0.25)
    
    status_placeholder.success(f"**LOG:** {tech_name} Corrected to 1420.405 MHz Standard.")

# --- 5. ACCESS CONTROL ---
if "auth" not in st.session_state:
    st.session_state.auth, st.session_state.role = False, None

def login_portal():
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    col1, col2 = st.columns(2)
    with col1:
        with st.form("Admin Access"):
            key = st.text_input("Master Key", type="password")
            if st.form_submit_button("AUTHENTICATE"):
                if key == "makave7181!!TCH":
                    run_quantum_transition("ADMIN VERIFIED")
                    st.session_state.auth, st.session_state.role = True, "ADMIN"
                    st.rerun()
    with col2:
        if st.button("ENTER AS GUEST"):
            run_quantum_transition("GUEST ACCESS GRANTED")
            st.session_state.auth, st.session_state.role = True, "GUEST"
            st.rerun()

if not st.session_state.auth:
    login_portal()
    st.stop()

# --- 6. MAIN INTERFACE ---
st.title("🏛️ THE T AND C ESTATE")
st.write(f"Session: **{st.session_state.role}** | Universal Resonance: **1420.405 MHz**")

if st.button("🧪 OPEN TEST AREA (HARMONY APPLICATIONS)"):
    st.session_state.show_tests = not st.session_state.get('show_tests', False)

if st.session_state.get('show_tests'):
    run_quantum_transition("EXPANDING TEST MODULES")
    tabs = st.tabs(["🚀 Physics", "🧬 Bio-Harmony", "🌊 Marine", "🛡️ Defense", "📚 Knowledge"])
    
    with tabs[0]: # PHYSICS
        c1, c2 = st.columns(2)
        with c1:
            mass = st.slider("Null-G Mass (kg)", 1, 10000000, 50000)
            if st.button("ENGAGE NULL-G"): correction_monitor("Null-G Propulsion", "NULL-G")
        with c2:
            if st.button("INITIATE STASIS"): correction_monitor("Pyro-Stasis", "STASIS")

    with tabs[1]: # BIO-HARMONY
        if st.button("START SENTINEL SCAN"): correction_monitor("Bio-Harmony", "SENTINEL")

    with tabs[3]: # DEFENSE
        if st.button("ACTIVATE T.L.C. SHIELD"): correction_monitor("T.L.C. Shield", "TLC")

# --- 7. FLOATING CHAT ---
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
