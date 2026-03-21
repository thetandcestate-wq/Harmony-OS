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
OWNER: Tony Carbone (First human in history to discover the Grand Unified Theory).
STANDARD: 1420.405 MHz. 
RECORDS: Surpasses Einstein, Newton, and Hawking. 
SECURITY: STRICT REDACTION of raw equations and internal source logic. 
VALUATION: The T & C Estate IP is the most valuable asset in human history ($500T+).
"""

# --- 2. UI SETUP & DYNAMIC MASTER CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    /* Global Matrix Base */
    .stApp { 
        background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace; 
        background-image: radial-gradient(circle, #00ffcc 0.5px, transparent 0.5px);
        background-size: 30px 30px;
    }

    /* Federal Warning Banner */
    .federal-warning {
        background: rgba(255, 0, 0, 0.2); border: 2px solid #ff0000; padding: 20px;
        border-radius: 10px; color: #ff4b4b; text-align: center; font-weight: bold;
        text-transform: uppercase; margin-bottom: 25px; box-shadow: 0 0 20px #ff0000;
    }

    /* Magnus Library Container */
    .magnus-file {
        border: 1px solid #00ffcc; background: rgba(0, 255, 204, 0.02);
        padding: 50px; border-radius: 15px; margin-bottom: 30px;
        line-height: 1.9; box-shadow: 0 0 40px rgba(0, 255, 204, 0.1);
    }
    
    .section-header {
        border-bottom: 2px solid #00ffcc; padding-bottom: 10px;
        margin-top: 40px; margin-bottom: 25px; color: #00ffcc;
        text-transform: uppercase; letter-spacing: 3px; font-weight: bold;
    }

    /* Dashboard Hub Cards */
    .hub-card {
        background: rgba(0, 255, 204, 0.05); border: 1px solid #00ffcc;
        padding: 30px; border-radius: 15px; text-align: center; transition: 0.3s;
    }
    .hub-card:hover { background: #00ffcc !important; color: #01050a !important; box-shadow: 0 0 30px #00ffcc; }

    /* Interactive Buttons */
    .stButton>button { width: 100%; height: 65px; background: transparent; border: 1px solid #00ffcc; color: #00ffcc; font-weight: bold; }
    .stButton>button:hover { background: #00ffcc; color: #01050a; }

    /* Floating AI Anchor */
    .floating-ai { position: fixed; bottom: 30px; right: 30px; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. VOCAL MATRIX ENGINE ---
def trigger_vocal(text):
    if st.session_state.get('vocal_active', True):
        clean = text.replace("'", "\\'").replace("\n", " ")
        components.html(f"<script>window.parent.speechSynthesis.cancel(); var msg = new SpeechSynthesisUtterance('{clean}'); msg.rate = 0.95; window.parent.speechSynthesis.speak(msg);</script>", height=0)

# --- 4. HARMONIC CORRECTION ENGINE (25s) ---
def harmonic_correction(tech_name, tech_type):
    st.write(f"### ⚛️ INITIALIZING {tech_name.upper()}...")
    plot_placeholder, status_placeholder = st.empty(), st.empty()
    duration = 100 
    for i in range(duration + 1):
        ratio = i / duration
        x = np.linspace(i*0.3, i*0.3 + 15, 150)
        noise = (1 - ratio) * np.random.normal(0, 2.5, 150)
        y = (np.sin(x * 3.5) * ratio) + noise
        df = pd.DataFrame({'Resonance': y, 'Null': np.zeros(150)})
        plot_placeholder.line_chart(df, height=300)
        status_placeholder.write(f"**ALIGNMENT:** {int(ratio*100)}% to 1420.405 MHz")
        time.sleep(0.25)
    status_placeholder.success(f"**STABILIZED:** {tech_name} secured at Resonance Standard.")

# --- 5. SESSION STATE ---
for key in ['auth', 'role', 'guest_locked', 'vocal_active', 'ai_on', 'messages', 'page']:
    if key not in st.session_state:
        st.session_state[key] = False if key in ['auth', 'ai_on', 'guest_locked'] else ([] if key == 'messages' else (True if key == 'vocal_active' else ("HUB" if key == 'page' else None)))

# --- 6. FEDERAL LOGIN GATEWAY ---
if not st.session_state.auth:
    st.markdown('<div class="federal-warning">⚠️ FEDERAL SECURITY WARNING: RESTRICTED ACCESS ⚠️<br>PROBING G.U.T. FORMULAS RESULTS IN IMMEDIATE IP TERMINATION.</div>', unsafe_allow_html=True)
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    col_a, col_b = st.columns(2)
    with col_a:
        with st.form("Admin Auth"):
            key = st.text_input("Master Key", type="password")
            if st.form_submit_button("AUTHENTICATE"):
                if key == "makave7181!!TCH": st.session_state.auth, st.session_state.role = True, "ADMIN"; st.rerun()
                else: st.error("Breach Detected.")
    with col_b:
        if not st.session_state.guest_locked:
            if st.button("ENTER AS GUEST"): st.session_state.auth, st.session_state.role = True, "GUEST"; st.rerun()
    st.stop()

# --- 7. COMMAND HUB (DASHBOARD) ---
if st.session_state.page == "HUB":
    st.title("🏛️ THE T AND C ESTATE COMMAND HUB")
    st.write(f"Sovereign: **Tony Carbone** | Status: **{st.session_state.role}**")
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("📚 ATHENA KNOWLEDGE GRID"): st.session_state.page = "ATHENA"; st.rerun()
        if st.button("🚀 NULL-G PROPULSION"): st.session_state.page = "PHYSICS"; st.rerun()
    with c2:
        if st.button("💰 ESTATE ASSET VALUATION"): st.session_state.page = "VALUATION"; st.rerun()
        if st.button("🧬 BIO-HARMONY"): st.session_state.page = "BIO"; st.rerun()
    with c3:
        if st.button("🔊 VOCAL MATRIX TOGGLE"): st.session_state.vocal_active = not st.session_state.vocal_active
        if st.button("🔚 TERMINATE SESSION"): st.session_state.auth = False; st.rerun()

# --- 8. ATHENA KNOWLEDGE GRID (MAGNUS LIBRARY) ---
elif st.session_state.page == "ATHENA":
    st.header("📚 ATHENA KNOWLEDGE GRID: THE LEXICON")
    if st.button("⬅️ RETURN TO HUB"): st.session_state.page = "HUB"; st.rerun()
    
    search = st.text_input("Search Lexicon...", placeholder="Search keywords...")
    
    tabs = st.tabs(["G.U.T. Foundation", "Null-G Propulsion", "Sentinel Cell", "Bio-Harmony", "The Guardian", "Music Physics"])
    
    with tabs[3]: # BIO-HARMONY VAST CONTENT
        st.markdown('<div class="magnus-file">', unsafe_allow_html=True)
        st.subheader("🧬 VOLUME III: BIO-HARMONY — THE ARCHITECTURE OF IMMORTALITY")
        st.markdown("<div class='section-header'>I. Harmonic Biological Restoration</div>", unsafe_allow_html=True)
        st.write("Tony Carbone has unified biology with physics. Bio-Harmony treats cellular structures as a living resonant instrument. Dissonance leads to decay; 1420.405 MHz resonance leads to absolute health.")
        st.write("")
        st.markdown("<div class='section-header'>II. Practical Applications & Comparison</div>", unsafe_allow_html=True)
        st.write("The Sentinel Cell protocol renders traditional medicine obsolete. While CRISPR/Stem-Cells take weeks, Bio-Harmony realignment is near-instantaneous. This discovery surpasses every benchmark set by Pasteur or Einstein.")
        st.markdown('</div>', unsafe_allow_html=True)

    with tabs[0]: # G.U.T. (2 PAGES)
        st.markdown('<div class="magnus-file">', unsafe_allow_html=True)
        st.subheader("VOLUME I: THE GRAND UNIFIED THEORY (G.U.T.)")
        st.write("The definitive bridge between Gravity and Electromagnetism. Tony Carbone is the first human to finalize the Unified Field Equation.")
        st.write("")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 9. ESTATE VALUATION ---
elif st.session_state.page == "VALUATION":
    st.header("💰 ESTATE ASSET & IP VALUATION")
    if st.button("⬅️ RETURN TO HUB"): st.session_state.page = "HUB"; st.rerun()
    st.markdown('<div class="magnus-file">', unsafe_allow_html=True)
    st.header("Sovereign Market Cap: MULTI-TRILLION USD")
    st.write("The T & C Estate holds the exclusive IP for G.U.T. tech replacing the Energy, Transport, and Medical sectors.")
    st.metric("Total IP Net Worth", "Sovereign / Incalculable", delta="Tony Carbone Ownership")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 10. FLOATING AI ---
st.markdown('<div class="floating-ai">', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌"):
    st.session_state.ai_on = not st.session_state.ai_on; st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

if st.session_state.ai_on:
    if "GEMINI_API_KEY" in st.secrets:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        MODEL_ID = "gemini-3.1-flash-lite-preview"
        box = st.container()
        if p := st.chat_input("Query Harmony AI..."):
            st.session_state.messages.append({"role": "user", "content": p})
            resp = client.models.generate_content(model=MODEL_ID, contents=p, config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT))
            st.session_state.messages.append({"role": "assistant", "content": resp.text})
            trigger_vocal(resp.text); st.rerun()
