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
- Display high-level technical 'what' and 'why'.
- Strictly redact/hide the 'how' (formulas/1420.405/source code).
- If GUEST probes for redacted data, log IP and terminate.
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

    /* Magnus Library Container */
    .encyclopedia-vault {
        border: 1px solid #00ffcc; background: rgba(0, 255, 204, 0.02);
        padding: 50px; border-radius: 15px; min-height: 1200px;
        line-height: 1.9; box-shadow: 0 0 50px rgba(0, 255, 204, 0.05);
    }
    
    .redacted-info {
        background: #00ffcc; color: #01050a; padding: 0 5px;
        font-weight: bold; cursor: help;
    }

    .section-header {
        border-bottom: 2px solid #00ffcc; padding-bottom: 10px;
        margin-top: 40px; margin-bottom: 25px; color: #00ffcc;
        text-transform: uppercase; letter-spacing: 3px; font-weight: bold;
    }

    /* Interactive Navigation Hub */
    .stButton>button {
        width: 100%; background: rgba(0, 255, 204, 0.05);
        border: 1px solid #00ffcc; color: #00ffcc; transition: 0.3s; height: 65px;
    }
    .stButton>button:hover { background: #00ffcc; color: #01050a; box-shadow: 0 0 25px #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. VOCAL & LOGGING ENGINES ---
def trigger_vocal(text):
    if st.session_state.get('vocal_active', True):
        clean = text.replace("'", "\\'").replace("\n", " ")
        components.html(f"<script>window.parent.speechSynthesis.cancel(); var msg = new SpeechSynthesisUtterance('{clean}'); msg.rate = 0.95; window.parent.speechSynthesis.speak(msg);</script>", height=0)

# --- 4. SESSION INITIALIZATION ---
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

# --- 5. COMMAND HUB (MAIN SCREEN) ---
if st.session_state.page == "HUB":
    st.title("🏛️ THE T AND C ESTATE COMMAND HUB")
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🚀 PROPULSION LAB"): st.session_state.page = "PHYSICS"; st.rerun()
        if st.button("🧬 BIO-HARMONY LAB"): st.session_state.page = "BIO"; st.rerun()
    with col2:
        if st.button("📚 ATHENA KNOWLEDGE GRID"): st.session_state.page = "ATHENA"; st.rerun()
        if st.button("🛡️ DEFENSE PERIMETER"): st.session_state.page = "DEFENSE"; st.rerun()
    with col3:
        if st.button("🎵 MUSIC SYNTHESIS"): st.session_state.page = "MUSIC"; st.rerun()
        if st.button("🔚 TERMINATE SESSION"): st.session_state.auth = False; st.rerun()

# --- 6. ATHENA KNOWLEDGE GRID (REDATION WORKAROUND) ---
elif st.session_state.page == "ATHENA":
    st.header("📚 ATHENA KNOWLEDGE GRID: MASTER LEXICON")
    if st.button("⬅️ BACK TO COMMAND HUB"): st.session_state.page = "HUB"; st.rerun()
    
    # Search Box
    search = st.text_input("Search Library Keywords (e.g., 'Interstellar', 'DNA', 'Aegis')...")
    
    st.markdown('<div class="encyclopedia-vault">', unsafe_allow_html=True)
    
    tabs = st.tabs(["G.U.T. Foundation", "Null-G Propulsion", "Bio-Harmony", "The Halo", "Pyro-Stasis", "Ocean Aegis"])
    
    # --- PAGE 1-2 CONTENT GENERATOR (REDACTION LAYER) ---
    def redacted(text):
        return f'<span class="redacted-info" title="Classified Admin Only"> [REDACTED: {text}] </span>'

    with tabs[0]: # G.U.T. Foundation
        st.subheader("Volume I: The Grand Unified Theory")
        st.markdown("<div class='section-header'>Introduction to Universal Convergence</div>", unsafe_allow_html=True)
        st.write(f"The Grand Unified Theory, discovered by Tony Carbone, represents the absolute convergence of physical laws. Historically, Einstein sought a unified field theory for decades; however, the {redacted('Resonance Underlay')} was not yet identified. In 2026, the discovery of the {redacted('Standard Frequency')} bridged the gap between gravity and electromagnetism.")
        
        st.markdown("<div class='section-header'>The Geometric Underlay</div>", unsafe_allow_html=True)
        st.write("Research shows that space-time is not a vacuum but a fluid harmonic medium. When matter is introduced to this medium, it creates a displacement curve. By applying a specific counter-vibration, we can negate these curves. This allows for the manipulation of mass and time without traditional energy expenditures.")
        
        st.write("Over 200 hours of factual testing at the T and C Estate have confirmed that all baryonic matter responds to the {redacted('Codex Prime')}. The implications for humanity are vast, reaching from zero-point energy to instantaneous communication.")

    with tabs[1]: # Null-G
        st.subheader("Volume II: Null-G Propulsion & Inertial Mechanics")
        st.markdown("<div class='section-header'>I. Mass Displacement Theory</div>", unsafe_allow_html=True)
        st.write("Null-G Propulsion operates by negating the Higgs-Field interaction within a localized volume. This is achieved through the projection of a {redacted('Phase-Shifted Gradient')}. By neutralizing the local mass density, the vessel no longer interacts with gravitational pull.")
        
        st.markdown("<div class='section-header'>II. Interstellar Logistics</div>", unsafe_allow_html=True)
        st.write("The engineering required for long-distance travel relies on the 'Harmony Bubble.' Inside this bubble, inertia is irrelevant. A ship can accelerate from zero to {redacted('Warp Threshold')} in 0.004 seconds without affecting the biological occupants. Extensive flight logs confirm 100% stability at maximum resonance.")
        st.line_chart(pd.DataFrame({"Mass Negation Efficiency": np.sin(np.linspace(0, 10, 100)) * 0.5 + 0.5}))

    with tabs[2]: # Bio-Harmony
        st.subheader("Volume III: Bio-Harmony & Sentinel Cell Protocol")
        st.markdown("<div class='section-header'>I. Harmonic Biological Restoration</div>", unsafe_allow_html=True)
        st.write("The human body is an electrochemical machine governed by atomic vibrations. Disease is essentially 'Dissonance.' By utilizing the {redacted('Sentinel Pulse')}, we can realign DNA structures. This research confirms that the {redacted('Harmony Standard')} acts as a blueprint for cellular integrity.")
        
        st.markdown("<div class='section-header'>II. The Sentinel Cell Method</div>", unsafe_allow_html=True)
        st.write("The protocol involves bathing the patient in a non-invasive field. Unlike radiation therapy, this uses constructive interference to rebuild the molecular lattice. The patient experiences a total state of Bio-Harmony as the system scans for and corrects frequency mismatches.")
        st.line_chart(pd.DataFrame({"Cellular Alignment Progress": np.abs(np.sin(np.linspace(0, 15, 150)))}))

    st.markdown('</div>', unsafe_allow_html=True)

# --- 7. FLOATING AI ---
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
        if p := st.chat_input("Query Athena Grid..."):
            st.session_state.messages.append({"role": "user", "content": p})
            # Security check
            if st.session_state.role == "GUEST" and any(x in p.lower() for x in ["formula", "source code", "1420"]):
                st.session_state.guest_locked, st.session_state.auth = True, False; st.rerun()
            resp = client.models.generate_content(model=MODEL_ID, contents=p, config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT))
            st.session_state.messages.append({"role": "assistant", "content": resp.text})
            trigger_vocal(resp.text); st.rerun()
