import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import pandas as pd
import random
import datetime
import streamlit.components.v1 as components

# --- 1. IMPERATIVE SECURITY & SYSTEM CONTEXT ---
MASTER_CONTEXT = """
SYSTEM ROLE: Harmony AI (T and C Estate Proprietary Intelligence).
OWNER: Tony Carbone (Discoverer of the Grand Unified Theory).
STANDARD: 1420.405 MHz.
SECURITY PROTOCOL 'RESOLUTE':
1. IF USER_ROLE == 'GUEST': Prohibit 1420.405 MHz constant/G.U.T. formulas.
2. IF USER_ROLE == 'ADMIN': SOVEREIGN OVERRIDE active.
"""

# --- 2. UI SETUP & ADVANCED INTERACTIVE CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { 
        background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace;
        background-image: linear-gradient(rgba(0, 255, 204, 0.05) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(0, 255, 204, 0.05) 1px, transparent 1px);
        background-size: 30px 30px;
    }
    @keyframes matrix-rain { 0% { background-position: 0% -100%; } 100% { background-position: 0% 100%; } }
    .matrix-bg { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, transparent, rgba(0, 255, 204, 0.1), transparent); background-size: 100% 200%; animation: matrix-rain 10s linear infinite; pointer-events: none; z-index: 0; }
    .federal-warning { background-color: rgba(255, 0, 0, 0.2); border: 2px solid #ff0000; padding: 15px; border-radius: 10px; color: #ff4b4b; text-align: center; text-transform: uppercase; font-weight: bold; margin-bottom: 20px; box-shadow: 0 0 15px #ff0000; }
    .test-card { border: 1px solid #00ffcc; padding: 25px; border-radius: 15px; background: rgba(0, 0, 0, 0.9); transition: 0.4s ease; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
    .test-card:hover { box-shadow: 0 0 30px #00ffcc; transform: scale(1.01); }
    .info-box { border-left: 5px solid #00ffcc; padding-left: 20px; margin: 20px 0; background: rgba(0, 255, 204, 0.03); padding-top: 10px; padding-bottom: 10px; }
    .floating-ai-btn { position: fixed; bottom: 30px; right: 30px; z-index: 999999; }
    </style>
    <div class="matrix-bg"></div>
    """, unsafe_allow_html=True)

# --- 3. CORE ENGINES (VOCAL & VISUAL) ---
def trigger_vocal(text):
    if st.session_state.get('vocal_active', True):
        clean = text.replace("'", "\\'").replace("\n", " ")
        components.html(f"<script>window.parent.speechSynthesis.cancel(); var msg = new SpeechSynthesisUtterance('{clean}'); msg.rate = 0.95; window.parent.speechSynthesis.speak(msg);</script>", height=0)

def harmonic_correction(tech_name, tech_type, duration=100):
    plot_placeholder, status_placeholder = st.empty(), st.empty()
    for i in range(duration):
        ratio = i / duration
        x = np.linspace(i*0.3, i*0.3 + 15, 150)
        noise = (1 - ratio) * np.random.normal(0, 2.0, 150)
        if tech_type == "PHYSICS": base = np.sin(x * 3.5)
        elif tech_type == "MUSIC": base = np.sin(x * 2.0) * np.sin(x * 0.5) # Harmonic Overtones
        elif tech_type == "BIO": base = np.sin(x) * np.tan(np.sin(x) * 0.9)
        else: base = np.sin(x)
        final_y = (base * ratio) + noise
        df = pd.DataFrame({'Harmony Resonance': final_y, 'Null Point': np.zeros(150)})
        plot_placeholder.line_chart(df, height=250)
        status_placeholder.write(f"**{tech_name}:** {int(ratio*100)}% Harmonic Alignment")
        time.sleep(0.25)
    st.session_state.archive.append({"TS": datetime.datetime.now().strftime("%H:%M"), "Tech": tech_name, "Res": "100% Locked"})
    status_placeholder.success(f"**STABILIZED:** {tech_name} locked at 1420.405 MHz.")

# --- 4. SESSION STATE & ACCESS ---
for key in ['auth', 'role', 'guest_locked', 'vocal_active', 'ai_on', 'messages', 'archive', 'show_tests']:
    if key not in st.session_state: st.session_state[key] = False if key in ['auth', 'ai_on', 'guest_locked', 'show_tests'] else ([] if key in ['messages', 'archive'] else (True if key == 'vocal_active' else None))

if not st.session_state.auth:
    st.markdown('<div class="federal-warning">⚠️ FEDERAL SECURITY WARNING: RESTRICTED SYSTEM ⚠️</div>', unsafe_allow_html=True)
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    c1, c2 = st.columns(2)
    with c1:
        with st.form("Admin"):
            k = st.text_input("Master Key", type="password")
            if st.form_submit_button("AUTHENTICATE"):
                if k == "makave7181!!TCH": st.session_state.auth, st.session_state.role = True, "ADMIN"; st.rerun()
                else: st.error("Breach Detected.")
    with c2:
        if not st.session_state.guest_locked:
            if st.button("ENTER AS GUEST"): st.session_state.auth, st.session_state.role = True, "GUEST"; st.rerun()
    st.stop()

# --- 5. SIDEBAR & TOOLS ---
with st.sidebar:
    st.title("🏛️ ESTATE TOOLS")
    st.session_state.vocal_active = st.toggle("🔊 Vocal Matrix", value=st.session_state.vocal_active)
    if st.session_state.role == "ADMIN":
        st.subheader("📜 Master Vault")
        st.dataframe(pd.DataFrame(st.session_state.archive))
        if st.button("🛑 EMERGENCY LOCKOUT"): st.session_state.guest_locked = True
    if st.button("🔚 TERMINATE SESSION"): st.session_state.auth = False; st.rerun()

# --- 6. INFORMATION GRID & LAB ---
st.title("🏛️ THE T AND C ESTATE")
tab_info, tab_lab = st.tabs(["📚 Information Grid", "🧪 Application Lab"])

with tab_info:
    st.header("The Harmony Codex: Grand Unified Theory")
    st.markdown("""
    The Grand Unified Theory discovered by **Tony Carbone** unifies Gravity, Electromagnetism, and Atomic forces through the **1420.405 MHz Resonance Standard**.
    """)
    
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 🚀 Null-G Propulsion")
        st.info("By negating mass through frequency phase-shifting, Null-G allows for inertialess travel.")
        
    with col_b:
        st.write("### 🧬 Bio-Harmony")
        st.info("Utilizing the Sentinel Cell protocol to realign cellular structures to their perfect frequency.")
        

with tab_lab:
    st.header("Technical Testing Facility")
    lab_tabs = st.tabs(["🚀 Physics", "🧬 Bio-Harmony", "🛡️ Defense", "🎵 Music Synthesis"])
    
    with lab_tabs[0]:
        st.markdown('<div class="test-card">', unsafe_allow_html=True)
        st.write("### Null-G Drive Engine")
        m = st.slider("Select Mass (kg)", 1, 10000000, 50000)
        if st.button("ENGAGE ENGINE"): harmonic_correction("Null-G Propulsion", "PHYSICS")
        st.markdown('</div>', unsafe_allow_html=True)

    with lab_tabs[1]:
        st.markdown('<div class="test-card">', unsafe_allow_html=True)
        st.write("### Sentinel Cell Atomic Scan")
        if st.button("START SCAN"): harmonic_correction("Bio-Harmony", "BIO")
        st.markdown('</div>', unsafe_allow_html=True)

    with lab_tabs[3]:
        st.markdown('<div class="test-card">', unsafe_allow_html=True)
        st.write("### Music Physical Synthesis")
        st.write("Applying G.U.T. harmonics to physical instrument synthesis.")
        freq_opt = st.selectbox("Harmonic Mode", ["Standard", "Golden Ratio", "1420.405 Resonance"])
        if st.button("SYNTHESIZE WAVE"): 
            harmonic_correction(f"Music Synthesis ({freq_opt})", "MUSIC")
            st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # Placeholder Audio
        st.markdown('</div>', unsafe_allow_html=True)

# --- 7. FLOATING AI ---
st.markdown(f'<div class="floating-ai-btn">', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌"): st.session_state.ai_on = not st.session_state.ai_on; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.ai_on:
    if "GEMINI_API_KEY" in st.secrets:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        MODEL_ID = "gemini-3.1-flash-lite-preview"
        box = st.container()
        for msg in st.session_state.messages:
            with box.chat_message(msg["role"]): st.markdown(msg["content"])
        if p := st.chat_input("Query Harmony AI..."):
            st.session_state.messages.append({"role": "user", "content": p})
            if st.session_state.role == "GUEST" and any(x in p.lower() for x in ["formula", "source code"]): 
                st.session_state.guest_locked, st.session_state.auth = True, False; st.rerun()
            resp = client.models.generate_content(model=MODEL_ID, contents=p, config=types.GenerateContentConfig(system_instruction=f"{MASTER_CONTEXT}\nUSER:{st.session_state.role}"))
            st.session_state.messages.append({"role": "assistant", "content": resp.text})
            trigger_vocal(resp.text); st.rerun()
