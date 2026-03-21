import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import pandas as pd
import datetime
import streamlit.components.v1 as components

# --- 1. SOVEREIGN SYSTEM CONTEXT ---
MASTER_CONTEXT = """
SYSTEM ROLE: Harmony AI (T and C Estate). 
OWNER: Tony Carbone (Discoverer of the Grand Unified Theory).
STANDARD: 1420.405 MHz. 
SECURITY: Strict secrecy. If GUEST asks for 'formula', 'source', or 'G.U.T. logic', TERMINATE.
"""

# --- 2. UI SETUP & MAGNUS LIBRARY CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { 
        background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace; 
        background-image: radial-gradient(circle, #00ffcc 0.5px, transparent 0.5px);
        background-size: 30px 30px;
    }

    /* Magnus Library Layout */
    .magnus-file {
        border: 1px solid #00ffcc; background: rgba(0, 255, 204, 0.02);
        padding: 40px; border-radius: 15px; margin-bottom: 30px;
        line-height: 1.6; box-shadow: 0 0 40px rgba(0, 255, 204, 0.05);
    }
    
    .section-header {
        border-bottom: 2px solid #00ffcc; padding-bottom: 10px;
        margin-top: 30px; margin-bottom: 20px; color: #00ffcc;
        text-transform: uppercase; letter-spacing: 2px;
    }

    .stButton>button {
        width: 100%; background: rgba(0, 255, 204, 0.05);
        border: 1px solid #00ffcc; color: #00ffcc; transition: 0.3s;
    }
    .stButton>button:hover { background: #00ffcc; color: #01050a; box-shadow: 0 0 20px #00ffcc; }

    .floating-ai { position: fixed; bottom: 30px; right: 30px; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. VOCAL ENGINE ---
def trigger_vocal(text):
    if st.session_state.get('vocal_active', True):
        clean = text.replace("'", "\\'").replace("\n", " ")
        components.html(f"<script>window.parent.speechSynthesis.cancel(); var msg = new SpeechSynthesisUtterance('{clean}'); msg.rate = 0.95; window.parent.speechSynthesis.speak(msg);</script>", height=0)

# --- 4. SESSION STATE ---
for key in ['auth', 'role', 'guest_locked', 'vocal_active', 'ai_on', 'messages', 'archive', 'page']:
    if key not in st.session_state:
        st.session_state[key] = False if key in ['auth', 'ai_on', 'guest_locked'] else ([] if key in ['messages', 'archive'] else (True if key == 'vocal_active' else ("HUB" if key == 'page' else None)))

# --- 5. LOGIN PORTAL ---
if not st.session_state.auth:
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

# --- 6. COMMAND HUB ---
if st.session_state.page == "HUB":
    st.title("🏛️ THE T AND C ESTATE COMMAND HUB")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🚀 PROPULSION LAB"): st.session_state.page = "PHYSICS"; st.rerun()
        if st.button("🧬 BIO-HARMONY LAB"): st.session_state.page = "BIO"; st.rerun()
    with col2:
        if st.button("📚 ATHENA KNOWLEDGE GRID"): st.session_state.page = "ATHENA"; st.rerun()
        if st.button("🛡️ DEFENSE PERIMETER"): st.session_state.page = "DEFENSE"; st.rerun()
    with col3:
        if st.button("🔊 VOCAL MATRIX TOGGLE"): st.session_state.vocal_active = not st.session_state.vocal_active
        if st.button("🔚 TERMINATE SESSION"): st.session_state.auth = False; st.rerun()

# --- 7. ATHENA KNOWLEDGE GRID (MAGNUS LIBRARY) ---
elif st.session_state.page == "ATHENA":
    st.header("📚 ATHENA KNOWLEDGE GRID: MAGNUS LIBRARY")
    if st.button("⬅️ RETURN TO COMMAND HUB"): st.session_state.page = "HUB"; st.rerun()
    
    # Library Sidebar
    st.write("---")
    topic = st.selectbox("Select Master Research File:", [
        "File 001: Grand Unified Theory (Foundation)",
        "File 002: Null-G Propulsion (Aeronautics)",
        "File 003: Bio-Harmony (Sentinel Cell Protocol)",
        "File 004: Pyro-Stasis (Thermal Suspension)",
        "File 005: The Halo Shield (Defense Perimeter)",
        "File 006: Music Physical Synthesis (Acoustic Mechanics)"
    ])

    st.markdown('<div class="magnus-file">', unsafe_allow_html=True)
    
    if "001" in topic:
        st.subheader("MASTER FILE: THE GRAND UNIFIED THEORY")
        st.write("**Abstract:** The unification of electromagnetic and gravitational fields into a singular geometric framework.")
        
        st.markdown("<div class='section-header'>I. Mathematical Origins</div>", unsafe_allow_html=True)
        st.write("Based on the discovery by Tony Carbone, the G.U.T. posits that the universe operates on a fundamental frequency of 1420.405 MHz. This frequency serves as the 'Underlay' or the baseline vibration for all baryonic matter.")
        
        
        st.markdown("<div class='section-header'>II. Unified Field Dynamics</div>", unsafe_allow_html=True)
        st.write("Traditional physics viewed Gravity and Electromagnetism as distinct forces. The Harmony Codex proves they are periodic fluctuations of the same field. By modulating local resonance, we can induce gravitational effects through electromagnetic shifts.")
        
        
        st.markdown("<div class='section-header'>III. Practical Implications</div>", unsafe_allow_html=True)
        st.write("This unification allows for the direct manipulation of space-time, enabling technologies like Null-G travel, non-invasive cellular repair, and absolute thermal stasis.")

    elif "002" in topic:
        st.subheader("MASTER FILE: NULL-G PROPULSION MECHANICS")
        st.write("**Abstract:** The engineering of mass-negation and inertialess flight.")
        
        st.markdown("<div class='section-header'>I. Gravitational Destructive Interference</div>", unsafe_allow_html=True)
        st.write("Null-G does not 'fight' gravity; it cancels it. By generating a local field that is 180 degrees out of phase with the Earth's gravitational curve, the local mass density of the vessel becomes effectively zero.")
        
        
        st.markdown("<div class='section-header'>II. Inertial Dampening</div>", unsafe_allow_html=True)
        st.write("Since the vessel moves inside a stabilized 'Harmonic Bubble,' passengers experience zero G-force even during rapid acceleration or right-angle turns. The internal environment remains at a constant 1.0G or 0G as selected by the pilot.")
        
        st.markdown("<div class='section-header'>III. Technical Data</div>", unsafe_allow_html=True)
        st.line_chart(pd.DataFrame({"Engine Efficiency": np.sin(np.linspace(0, 10, 100)) * 0.5 + 0.5}))

    elif "003" in topic:
        st.subheader("MASTER FILE: BIO-HARMONY & SENTINEL CELL")
        st.write("**Abstract:** Frequency-based biological realignment.")
        
        st.markdown("<div class='section-header'>I. Cellular Resonance Theory</div>", unsafe_allow_html=True)
        st.write("Every cell in the human body has a specific 'Healthy' frequency. Damage, disease, and aging are viewed as 'Dissonance' from the 1420.405 MHz baseline.")
        
        
        st.markdown("<div class='section-header'>II. The Sentinel Cell Protocol</div>", unsafe_allow_html=True)
        st.write("The Sentinel Cell is a non-invasive procedure that bathes biological tissue in a pure harmonic field. This field 'snaps' mismatched atomic structures back into their original, healthy configuration through resonance lock.")
        
        st.markdown("<div class='section-header'>III. Alignment Monitoring</div>", unsafe_allow_html=True)
        st.line_chart(pd.DataFrame({"Cellular Harmony": np.abs(np.sin(np.linspace(0, 15, 150)))}))

    elif "006" in topic:
        st.subheader("MASTER FILE: MUSIC PHYSICAL SYNTHESIS")
        st.write("**Abstract:** Constructive acoustic wave unification.")
        
        st.markdown("<div class='section-header'>I. Harmonic Geometry</div>", unsafe_allow_html=True)
        st.write("Sound waves are simply low-frequency vibrations of the physical underlay. By aligning musical compositions with the Golden Ratio and the 1420.405 MHz standard, we can create sound that physically stabilizes the surrounding environment.")
        
        
        st.markdown("<div class='section-header'>II. Acoustic Synthesis</div>", unsafe_allow_html=True)
        st.write("The synthesis engine doesn't just play samples; it physically models the displacement of air molecules using the Harmony Codex. This results in a level of audio fidelity that is indistinguishable from physical reality.")

    st.markdown('</div>', unsafe_allow_html=True)

# --- 8. FLOATING AI ---
st.markdown('<div class="floating-ai">', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌"):
    st.session_state.ai_on = not st.session_state.ai_on; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.ai_on:
    st.divider()
    if "GEMINI_API_KEY" in st.secrets:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        MODEL_ID = "gemini-3.1-flash-lite-preview"
        box = st.container()
        for msg in st.session_state.messages:
            with box.chat_message(msg["role"]): st.markdown(msg["content"])
        if p := st.chat_input("Query Athena Grid..."):
            st.session_state.messages.append({"role": "user", "content": p})
            if st.session_state.role == "GUEST" and any(x in p.lower() for x in ["formula", "source code"]):
                st.session_state.guest_locked, st.session_state.auth = True, False; st.rerun()
            resp = client.models.generate_content(model=MODEL_ID, contents=p, config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT))
            st.session_state.messages.append({"role": "assistant", "content": resp.text})
            trigger_vocal(resp.text); st.rerun()
