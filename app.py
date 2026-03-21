import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import pandas as pd
import datetime
import streamlit.components.v1 as components

# --- 1. SOVEREIGN SECURITY CONTEXT ---
MASTER_CONTEXT = """
SYSTEM ROLE: Harmony AI. OWNER: Tony Carbone (G.U.T. Discoverer).
SECURITY: 'OBSIDIAN' PROTOCOL ACTIVE. 
- Display vast technical descriptions of 'what' and 'why'.
- Redact the 'how' (specific 1420.405 formulas/source code).
"""

# --- 2. UI SETUP & ENCYCLOPEDIA CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { 
        background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace; 
        background-image: radial-gradient(circle, #00ffcc 0.4px, transparent 0.4px);
        background-size: 30px 30px;
    }
    .encyclopedia-vault {
        border: 1px solid #00ffcc; background: rgba(0, 255, 204, 0.02);
        padding: 50px; border-radius: 15px; min-height: 1200px;
        line-height: 1.9; box-shadow: 0 0 50px rgba(0, 255, 204, 0.05);
    }
    .redacted { background: #00ffcc; color: #01050a; padding: 0 5px; font-weight: bold; }
    .section-header {
        border-bottom: 2px solid #00ffcc; padding-bottom: 10px;
        margin-top: 40px; margin-bottom: 25px; color: #00ffcc;
        text-transform: uppercase; letter-spacing: 3px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. REDACTION UTILITY ---
def redact(text):
    return f'<span class="redacted" title="Classified Admin Only"> [REDACTED: {text}] </span>'

# --- 4. SESSION STATE & LOGIN ---
for key in ['auth', 'role', 'guest_locked', 'vocal_active', 'ai_on', 'messages', 'archive', 'page']:
    if key not in st.session_state:
        st.session_state[key] = False if key in ['auth', 'ai_on', 'guest_locked'] else ([] if key in ['messages', 'archive'] else (True if key == 'vocal_active' else ("HUB" if key == 'page' else None)))

if not st.session_state.auth:
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    c1, c2 = st.columns(2)
    with c1:
        with st.form("Admin"):
            if st.form_submit_button("ADMIN AUTH"):
                st.session_state.auth, st.session_state.role = True, "ADMIN"; st.rerun()
    with c2:
        if not st.session_state.guest_locked:
            if st.button("ENTER AS GUEST"): st.session_state.auth, st.session_state.role = True, "GUEST"; st.rerun()
    st.stop()

# --- 5. COMMAND HUB ---
if st.session_state.page == "HUB":
    st.title("🏛️ THE T AND C ESTATE COMMAND HUB")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📚 ATHENA KNOWLEDGE GRID"): st.session_state.page = "ATHENA"; st.rerun()
    with col2:
        if st.button("🔚 TERMINATE SESSION"): st.session_state.auth = False; st.rerun()

# --- 6. ATHENA KNOWLEDGE GRID (NEW VOLUMES) ---
elif st.session_state.page == "ATHENA":
    st.header("📚 ATHENA KNOWLEDGE GRID: MASTER LEXICON")
    if st.button("⬅️ BACK TO HUB"): st.session_state.page = "HUB"; st.rerun()
    
    st.markdown('<div class="encyclopedia-vault">', unsafe_allow_html=True)
    tabs = st.tabs(["The Halo Shield", "Pyro-Stasis", "Ocean Aegis", "G.U.T. Basics"])
    
    with tabs[0]: # THE HALO
        st.subheader("Volume IV: The Halo & T.L.C. Perimeter")
        st.markdown("<div class='section-header'>I. Defensive Refractive Geometry</div>", unsafe_allow_html=True)
        st.write(f"The Halo Shield is a standing-wave refractive perimeter designed to neutralize incoming kinetic and energy-based threats. By utilizing the {redact('Phase-Shift Modulation')}, the shield does not absorb impact but rather 'refracts' space-time around the protected zone. This creates a localized curvature where external vectors are grounded into the {redact('Planetary Resonance')}.")
        [attachment_0](attachment)
        st.markdown("<div class='section-header'>II. T.L.C. Integration</div>", unsafe_allow_html=True)
        st.write("Total Logistical Containment (T.L.C.) ensures that the internal harmonic state of the Estate remains constant. Even under massive external bombardment, the internal atmosphere, pressure, and {redact('Baseline Frequency')} remain undisturbed.")

    with tabs[1]: # PYRO-STASIS
        st.subheader("Volume V: Pyro-Stasis & Thermal Suspension")
        st.markdown("<div class='section-header'>I. Atomic Motion Cessation</div>", unsafe_allow_html=True)
        st.write(f"Pyro-Stasis is the active removal of entropy from a closed system. By locking molecular structures to the {redact('Static Harmonic Code')}, atoms are prevented from vibrating. As heat is fundamentally the vibration of particles, locking them into a {redact('Fixed Lattice')} effectively creates a state of zero thermal activity.")
        
        st.markdown("<div class='section-header'>II. Preservation Logistics</div>", unsafe_allow_html=True)
        st.write("This vast research proves that organic matter can be maintained in this state indefinitely. This allows for long-term storage of volatile materials and is a cornerstone for deep-space biological preservation.")

    with tabs[2]: # OCEAN AEGIS
        st.subheader("Volume VI: Ocean Aegis & Marine Aegis")
        st.markdown("<div class='section-header'>I. Sub-Aquatic Harmonic Pressure Shielding</div>", unsafe_allow_html=True)
        st.write(f"Ocean Aegis applies the Grand Unified Theory to marine environments. By modulating the {redact('Hydraulic Resonance')}, the system can equalize external water pressure, allowing for deep-sea structures to exist without massive structural reinforcement. The system creates a 'Pressure-Neutral Bubble' around sub-aquatic labs.")
        
        st.markdown("<div class='section-header'>II. Acoustic Neutralization</div>", unsafe_allow_html=True)
        st.write("Furthermore, Ocean Aegis utilizes {redact('Sonar Destructive Interference')} to render the Estate's marine presence invisible to traditional sonar detection systems.")

    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. FLOATING AI ---
st.markdown('<div style="position:fixed; bottom:30px; right:30px; z-index:999;">', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI"): st.session_state.ai_on = not st.session_state.ai_on; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)
