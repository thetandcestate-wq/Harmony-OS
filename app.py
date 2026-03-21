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
Applications: Null-G, Pyro-Stasis, Bio-Harmony (Sentinel Cell), The Halo.
Tone: Professional, authoritative, and paramount.
"""

# --- 2. UI SETUP & SCIFI CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { background-color: #01080e; color: #00ffcc; font-family: 'Courier New', Courier, monospace; }
    
    /* G.U.T. Scanner Animation */
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
            "Calculating Gravitational Constant Variance...",
            "Resonance Lock: 1420.405 MHz Verified.",
            "Synthesizing Grand Unified Field Equation...",
            "Underlay Protocol: Status Paramount.",
            "T.L.C. Security Shield: Active."
        ]
        for eq in equations:
            st.code(f">>> {eq}", language=None)
            time.sleep(0.8)
    placeholder.empty()

# --- 4. LIVE FREQUENCY VISUALIZERS ---
def live_monitor(type="SINE", duration=30):
    plot_placeholder = st.empty()
    t = 0
    for _ in range(duration):
        t += 0.3
        x = np.linspace(t, t + 15, 150)
        
        if type == "NULL-G":
            # Fast, tight wave representing mass negation
            y = np.sin(x * 2.5)
        elif type == "BIO":
            # Sharp spikes representing atomic realignment
            y = np.sin(x) * np.tan(np.sin(x) * 0.9) 
        elif type == "HALO":
            # Broad pulsing waves representing shield perimeter
            y = np.sin(x) * np.exp(-np.power((x % 8 - 4), 2) / 4)
        else:
            y = np.sin(x)
            
        null_line = np.zeros(150)
        df = pd.DataFrame({'Resonance': y, 'Null Point': null_line})
        plot_placeholder.line_chart(df, height=200)
        time.sleep(0.05)

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

# --- 7. CONSOLIDATED TEST AREA ---
if st.button("🧪 OPEN TEST AREA (HARMONY APPLICATIONS)"):
    st.session_state.show_tests = not st.session_state.get('show_tests', False)

if st.session_state.get('show_tests'):
    st.markdown("---")
    tabs = st.tabs(["🚀 Null-G", "🧬 Bio-Harmony", "🛡️ The Halo"])
    
    with tabs[0]:
        st.subheader("Null-G Propulsion Simulation")
        mass_kg = st.slider("Select Vessel Mass (kg)", 1, 10000000, 50000)
        if st.button("ENGAGE MASS NEGATION"):
            st.metric("Effective Mass", f"{mass_kg * 1e-8:.8f} kg")
            live_monitor("NULL-G")

    with tabs[1]:
        st.subheader("Bio-Harmony: Atomic Realignment")
        st.write("Sentinel Cell Correction Protocol: 1420.405 MHz")
        if st.button("INITIATE ATOMIC SCAN"):
            live_monitor("BIO")
            st.success("Cellular frequency corrected to Harmonic Standard.")

    with tabs[2]:
        st.subheader("The Halo: Perimeter Shielding")
        if st.button("TEST SHIELD MODULATION"):
            live_monitor("HALO")
            st.warning("Perimeter Integrity: 100% Operational.")

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
