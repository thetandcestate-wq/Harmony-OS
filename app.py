import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import pandas as pd
import random
import datetime
import streamlit.components.v1 as components

# --- 1. SOVEREIGN SYSTEM CONTEXT ---
MASTER_CONTEXT = """
SYSTEM ROLE: Harmony AI (T and C Estate). OWNER: Tony Carbone.
STANDARD: 1420.405 MHz. G.U.T. Signature: Verified.
SECURITY: Immediate IP Termination for GUEST probing of formulas/source.
"""

# --- 2. UI SETUP & DYNAMIC MODULAR CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    /* Global Matrix Base */
    .stApp { background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace; }
    
    /* Dynamic Screen Skins */
    .physics-skin { border: 2px solid #00ffcc; padding: 30px; background: rgba(0, 255, 204, 0.02); border-radius: 20px; box-shadow: inset 0 0 50px rgba(0, 255, 204, 0.1); }
    .bio-skin { border: 2px solid #00ffcc; padding: 30px; background: radial-gradient(circle, rgba(0,255,204,0.1) 0%, rgba(1,5,10,1) 100%); border-radius: 50% 20px; }
    .music-skin { border-left: 10px solid #00ffcc; padding: 30px; background: repeating-linear-gradient(45deg, #01050a, #01050a 10px, rgba(0,255,204,0.05) 10px, rgba(0,255,204,0.05) 20px); }
    .defense-skin { border: 1px solid #ff4b4b; padding: 30px; background: rgba(255, 75, 75, 0.05); box-shadow: 0 0 40px rgba(255, 75, 75, 0.2); }

    /* Interactive Elements */
    .stButton>button { width: 100%; background: transparent; border: 1px solid #00ffcc; color: #00ffcc; transition: 0.3s; text-transform: uppercase; }
    .stButton>button:hover { background: #00ffcc; color: #01050a; box-shadow: 0 0 30px #00ffcc; }
    
    .floating-ai { position: fixed; bottom: 30px; right: 30px; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. VOCAL & ANIMATION LOGIC ---
def trigger_vocal(text):
    if st.session_state.get('vocal_active', True):
        clean = text.replace("'", "\\'").replace("\n", " ")
        components.html(f"<script>window.parent.speechSynthesis.cancel(); var msg = new SpeechSynthesisUtterance('{clean}'); msg.rate = 0.9; window.parent.speechSynthesis.speak(msg);</script>", height=0)

def harmonic_correction(tech_name, tech_type):
    plot_placeholder, status_placeholder = st.empty(), st.empty()
    for i in range(101):
        ratio = i / 100
        x = np.linspace(i*0.3, i*0.3 + 15, 150)
        noise = (1 - ratio) * np.random.normal(0, 2.0, 150)
        if tech_type == "PHYSICS": y = (np.sin(x * 3.5) * ratio) + noise
        elif tech_type == "MUSIC": y = ((np.sin(x * 2.0) * np.sin(x * 0.5)) * ratio) + noise
        elif tech_type == "BIO": y = ((np.sin(x) * np.tan(np.sin(x) * 0.8)) * ratio) + noise
        else: y = (np.sin(x) * ratio) + noise
        df = pd.DataFrame({'Resonance': y, 'Null': np.zeros(150)})
        plot_placeholder.line_chart(df, height=250)
        status_placeholder.write(f"**{tech_name}:** {i}% Aligned")
        time.sleep(0.2)
    st.session_state.archive.append({"TS": datetime.datetime.now().strftime("%H:%M"), "Tech": tech_name})
    status_placeholder.success(f"**STABILIZED:** {tech_name} locked at 1420.405 MHz.")

# --- 4. SESSION STATE ---
for key in ['auth', 'role', 'guest_locked', 'vocal_active', 'ai_on', 'messages', 'archive', 'page']:
    if key not in st.session_state:
        st.session_state[key] = False if key in ['auth', 'ai_on', 'guest_locked'] else ([] if key in ['messages', 'archive'] else (True if key == 'vocal_active' else ("HOME" if key == 'page' else None)))

# --- 5. FEDERAL LOGIN PORTAL ---
if not st.session_state.auth:
    st.markdown('<div class="defense-skin" style="text-align:center; color:#ff4b4b;">⚠️ FEDERAL SECURITY WARNING: IP LOGGING ACTIVE ⚠️</div>', unsafe_allow_html=True)
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    c1, c2 = st.columns(2)
    with c1:
        with st.form("Admin"):
            k = st.text_input("Master Key", type="password")
            if st.form_submit_button("AUTHENTICATE"):
                if k == "makave7181!!TCH": st.session_state.auth, st.session_state.role = True, "ADMIN"; st.rerun()
    with c2:
        if not st.session_state.guest_locked:
            if st.button("ENTER AS GUEST"): st.session_state.auth, st.session_state.role = True, "GUEST"; st.rerun()
    st.stop()

# --- 6. COMMAND HUB (SIDEBAR) ---
with st.sidebar:
    st.title("🏛️ COMMAND HUB")
    st.write(f"Status: **{st.session_state.role}**")
    st.write("---")
    
    # Navigation Buttons
    if st.button("🛰️ DASHBOARD"): st.session_state.page = "HOME"
    if st.button("🚀 NULL-G PROPULSION"): st.session_state.page = "PHYSICS"
    if st.button("🧬 BIO-HARMONY"): st.session_state.page = "BIO"
    if st.button("🛡️ THE HALO / TLC"): st.session_state.page = "DEFENSE"
    if st.button("🎵 MUSIC SYNTHESIS"): st.session_state.page = "MUSIC"
    
    st.write("---")
    st.subheader("System Toggles")
    st.session_state.vocal_active = st.toggle("🔊 Vocal Matrix", value=st.session_state.vocal_active)
    
    if st.session_state.role == "ADMIN":
        st.subheader("📜 Master Vault")
        st.dataframe(pd.DataFrame(st.session_state.archive))
        if st.button("🛑 EMERGENCY LOCK"): st.session_state.guest_locked = True
    
    if st.button("🔚 LOGOUT"):
        st.session_state.auth = False
        st.rerun()

# --- 7. MODULAR MAIN SCREENS ---
if st.session_state.page == "HOME":
    st.title("🏛️ ESTATE DASHBOARD")
    st.markdown('<div class="physics-skin">', unsafe_allow_html=True)
    st.header("Welcome, Tony Carbone")
    st.write("The Grand Unified Theory is currently active across all sectors at 1420.405 MHz.")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "PHYSICS":
    st.title("🚀 NULL-G PROPULSION LAB")
    st.markdown('<div class="physics-skin">', unsafe_allow_html=True)
    m = st.slider("Select Vessel Mass (kg)", 1, 10000000, 50000)
    if st.button("ENGAGE MASS NEGATION"): harmonic_correction("Null-G Propulsion", "PHYSICS")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "BIO":
    st.title("🧬 BIO-HARMONY (SENTINEL CELL)")
    st.markdown('<div class="bio-skin">', unsafe_allow_html=True)
    if st.button("INITIATE ATOMIC SCAN"): harmonic_correction("Bio-Harmony", "BIO")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "MUSIC":
    st.title("🎵 MUSIC PHYSICAL SYNTHESIS")
    st.markdown('<div class="music-skin">', unsafe_allow_html=True)
    st.write("Harmonizing the Golden Ratio with 1420.405 MHz Resonance.")
    if st.button("SYNTHESIZE WAVEFORM"): harmonic_correction("Music Synthesis", "MUSIC")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "DEFENSE":
    st.title("🛡️ T.L.C. SHIELD / THE HALO")
    st.markdown('<div class="defense-skin">', unsafe_allow_html=True)
    if st.button("MODULATE PERIMETER"): harmonic_correction("The Halo Shield", "DEFENSE")
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- 8. FLOATING AI ---
st.markdown('<div class="floating-ai">', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌"):
    st.session_state.ai_on = not st.session_state.ai_on
    st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.ai_on:
    st.divider()
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
            resp = client.models.generate_content(model=MODEL_ID, contents=p, config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT))
            st.session_state.messages.append({"role": "assistant", "content": resp.text})
            trigger_vocal(resp.text); st.rerun()
