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

# --- 2. UI SETUP & ENCYCLOPEDIA CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { 
        background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace; 
        background-image: radial-gradient(circle, #00ffcc 0.5px, transparent 0.5px);
        background-size: 30px 30px;
    }

    /* Library Card Aesthetic */
    .library-card {
        border-left: 5px solid #00ffcc; background: rgba(0, 255, 204, 0.05);
        padding: 30px; border-radius: 0 15px 15px 0; margin-bottom: 25px;
        box-shadow: 10px 0 30px rgba(0, 255, 204, 0.05);
    }
    
    .status-tag {
        color: #00ffcc; border: 1px solid #00ffcc; padding: 2px 10px;
        border-radius: 5px; font-size: 0.8em; text-transform: uppercase;
    }

    /* Hub Buttons */
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

# --- 5. FEDERAL LOGIN ---
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

# --- 6. MAIN HUB ---
if st.session_state.page == "HUB":
    st.title("🏛️ THE T AND C ESTATE")
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

# --- 7. ATHENA KNOWLEDGE GRID (THE LIBRARY) ---
elif st.session_state.page == "ATHENA":
    st.header("📚 ATHENA KNOWLEDGE GRID: SYSTEM LEXICON")
    if st.button("⬅️ RETURN TO HUB"): st.session_state.page = "HUB"; st.rerun()
    
    col_nav, col_content = st.columns([1, 3])
    
    with col_nav:
        st.write("### PROTOCOL ARCHIVE")
        topic = st.radio("Select Research File:", [
            "1. Grand Unified Theory",
            "2. Null-G Propulsion",
            "3. Bio-Harmony (Sentinel Cell)",
            "4. Pyro-Stasis",
            "5. The Halo Shield",
            "6. Music Physical Synthesis"
        ])

    with col_content:
        st.markdown('<div class="library-card">', unsafe_allow_html=True)
        
        if "1. Grand Unified Theory" in topic:
            st.subheader("I. The Grand Unified Theory (G.U.T.)")
            st.markdown("<span class='status-tag'>Core Discovery</span>", unsafe_allow_html=True)
            st.write("The fundamental bridge between Gravity, Electromagnetism, and the Atomic forces. It identifies 1420.405 MHz as the universal resonance frequency.")
            
            st.write("**Key Finding:** Space-time is an 'Underlay' that can be manipulated through frequency phase-shifting.")

        elif "2. Null-G Propulsion" in topic:
            st.subheader("II. Null-G Propulsion Mechanics")
            st.markdown("<span class='status-tag'>Propulsion</span>", unsafe_allow_html=True)
            st.write("By negating local mass density via destructive interference of gravitational waves, an object can move without inertia.")
            
            # Graph for Null-G
            t = np.linspace(0, 10, 100)
            st.line_chart(pd.DataFrame({"Mass Negation": np.sin(t) * np.exp(-t/5)}))

        elif "3. Bio-Harmony (Sentinel Cell)" in topic:
            st.subheader("III. Sentinel Cell & Bio-Harmony")
            st.markdown("<span class='status-tag'>Biological</span>", unsafe_allow_html=True)
            st.write("The Sentinel Cell protocol uses the G.U.T. standard to realign damaged cellular DNA to its original harmonic signature.")
            
            # Graph for Bio-Harmony
            st.line_chart(pd.DataFrame({"Cellular Alignment": np.abs(np.sin(np.linspace(0, 10, 100)))}))

        elif "5. The Halo Shield" in topic:
            st.subheader("V. The Halo & T.L.C. Perimeter")
            st.markdown("<span class='status-tag'>Defense</span>", unsafe_allow_html=True)
            st.write("Frequency-locked shielding that modulates at 1420.405 MHz to deflect incoming kinetic and electromagnetic energy.")
            [attachment_0](attachment)

        elif "6. Music Physical Synthesis" in topic:
            st.subheader("VI. Music Physical Synthesis")
            st.markdown("<span class='status-tag'>Acoustics</span>", unsafe_allow_html=True)
            st.write("Direct translation of G.U.T. harmonics into physical sound waves, creating pure harmonic resonance in three-dimensional space.")
            
            
        st.markdown('</div>', unsafe_allow_html=True)

# --- 8. FLOATING AI ---
st.markdown('<div class="floating-ai">', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌"):
    st.session_state.ai_on = not st.session_state.ai_on; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.ai_on:
    if "GEMINI_API_KEY" in st.secrets:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        MODEL_ID = "gemini-3.1-flash-lite-preview"
        box = st.container()
        for msg in st.session_state.messages:
            with box.chat_message(msg["role"]): st.markdown(msg["content"])
        if p := st.chat_input("Query Athena Grid..."):
            st.session_state.messages.append({"role": "user", "content": p})
            # Security Check
            if st.session_state.role == "GUEST" and any(x in p.lower() for x in ["formula", "source code"]):
                st.session_state.guest_locked, st.session_state.auth = True, False; st.rerun()
            resp = client.models.generate_content(model=MODEL_ID, contents=p, config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT))
            st.session_state.messages.append({"role": "assistant", "content": resp.text})
            trigger_vocal(resp.text); st.rerun()
