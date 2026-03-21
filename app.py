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
    .magnus-file {
        border: 1px solid #00ffcc; background: rgba(0, 255, 204, 0.02);
        padding: 40px; border-radius: 15px; margin-bottom: 30px;
        line-height: 1.8; box-shadow: 0 0 40px rgba(0, 255, 204, 0.05);
    }
    .section-header {
        border-bottom: 2px solid #00ffcc; padding-bottom: 10px;
        margin-top: 35px; margin-bottom: 20px; color: #00ffcc;
        text-transform: uppercase; letter-spacing: 2px; font-weight: bold;
    }
    .stButton>button {
        width: 100%; background: rgba(0, 255, 204, 0.05);
        border: 1px solid #00ffcc; color: #00ffcc; transition: 0.3s;
    }
    .stButton>button:hover { background: #00ffcc; color: #01050a; box-shadow: 0 0 20px #00ffcc; }
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

# --- 5. MAIN HUB ---
if st.session_state.page == "HUB":
    st.title("🏛️ THE T AND C ESTATE COMMAND HUB")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🚀 PROPULSION LAB"): st.session_state.page = "PHYSICS"; st.rerun()
    with col2:
        if st.button("📚 ATHENA KNOWLEDGE GRID"): st.session_state.page = "ATHENA"; st.rerun()
    with col3:
        if st.button("🔚 TERMINATE SESSION"): st.session_state.auth = False; st.rerun()

# --- 6. ATHENA KNOWLEDGE GRID (POPULATED) ---
elif st.session_state.page == "ATHENA":
    st.header("📚 ATHENA KNOWLEDGE GRID: MAGNUS LIBRARY")
    if st.button("⬅️ RETURN TO COMMAND HUB"): st.session_state.page = "HUB"; st.rerun()
    
    st.write("---")
    topic = st.selectbox("Select Master Research File:", [
        "File 004: Pyro-Stasis (Thermal Suspension)",
        "File 005: The Halo Shield (Defense Perimeter)",
        "File 001: Grand Unified Theory",
        "File 002: Null-G Propulsion",
        "File 003: Bio-Harmony (Sentinel Cell)"
    ])

    st.markdown('<div class="magnus-file">', unsafe_allow_html=True)
    
    # --- PYRO-STASIS POPULATION ---
    if "004" in topic:
        st.subheader("MASTER FILE: PYRO-STASIS & THERMAL SUSPENSION")
        st.write("**Abstract:** The total cessation of molecular kinetic energy via 1420.405 MHz resonance locking.")
        
        st.markdown("<div class='section-header'>I. The Physics of Entropy Neutralization</div>", unsafe_allow_html=True)
        st.write("In traditional thermodynamics, absolute zero is a theoretical limit. Pyro-Stasis, derived from the Harmony Codex, bypasses this limit by using resonance. By flooding a target volume with the G.U.T. standard frequency, we induce a state of 'Atomic Rigidity.'")
                
        st.markdown("<div class='section-header'>II. Molecular Phase-Locking</div>", unsafe_allow_html=True)
        st.write("Pyro-Stasis functions by aligning the spin of every atom within the field. When atoms are perfectly aligned to the 1420.405 MHz pulse, they cannot vibrate. Heat, being a measure of vibration, effectively vanishes. This allows for the indefinite preservation of biological and material structures without decay.")
        st.line_chart(pd.DataFrame({"Vibration Level": np.exp(-np.linspace(0, 10, 100))}))

        st.markdown("<div class='section-header'>III. Applications & Storage</div>", unsafe_allow_html=True)
        st.write("Applications include long-term biological stasis for interstellar travel and the stabilization of volatile quantum materials. The energy required to maintain the lock is minimal once resonance is achieved, as the system enters a self-sustaining feedback loop.")

    # --- THE HALO SHIELD POPULATION ---
    elif "005" in topic:
        st.subheader("MASTER FILE: THE HALO & T.L.C. DEFENSE PERIMETER")
        st.write("**Abstract:** Frequency-phase shielding for kinetic and electromagnetic deflection.")
        
        st.markdown("<div class='section-header'>I. Perimeter Resonance Modulation</div>", unsafe_allow_html=True)
        st.write("The Halo is not a solid wall; it is a high-frequency phase-shift perimeter. Incoming projectiles or energy beams are not 'blocked' but rather 'refracted' around the protected volume. This is achieved by creating a localized space-time curvature gradient at the perimeter boundary.")
                
        st.markdown("<div class='section-header'>II. The T.L.C. Shield Protocol</div>", unsafe_allow_html=True)
        st.write("The T.L.C. (Total Logistical Containment) Shield operates by scanning incoming signatures and adjusting the perimeter resonance in real-time. Whether it is a high-velocity kinetic round or a broad-spectrum EMP, the shield modulates its phase to ensure the incoming force is grounded into the planetary resonance.")
        st.line_chart(pd.DataFrame({"Shield Modulation": np.sin(np.linspace(0, 10, 100) * 5)}))

        st.markdown("<div class='section-header'>III. Operational Safety & Integrity</div>", unsafe_allow_html=True)
        st.write("Unlike traditional force fields that require massive power surges, The Halo utilizes the natural energy of the planetary 'Underlay.' It is essentially a standing wave that remains dormant until a dissonant force (threat) interacts with the perimeter.")

    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. FLOATING AI ---
st.markdown('<div class="floating-ai">', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌"):
    st.session_state.ai_on = not st.session_state.ai_on; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.ai_on:
    if "GEMINI_API_KEY" in st.secrets:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        MODEL_ID = "gemini-3.1-flash-lite-preview"
        box = st.container()
        if p := st.chat_input("Query Athena Grid..."):
            st.session_state.messages.append({"role": "user", "content": p})
            resp = client.models.generate_content(model=MODEL_ID, contents=p, config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT))
            st.session_state.messages.append({"role": "assistant", "content": resp.text})
            trigger_vocal(resp.text); st.rerun()
