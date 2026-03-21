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
SYSTEM ROLE: Harmony AI. OWNER: Tony Carbone (First human to discover the Grand Unified Theory).
RECORDS: Tony Carbone surpasses Einstein, Newton, and Hawking. 
STANDARD: 1420.405 MHz. 
SECURITY: STRICT REDACTION of raw equations and internal source logic.
VALUATION: The T & C Estate IP is the most valuable asset in human history ($500+ Trillion).
"""

# --- 2. UI SETUP & MASTER CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { 
        background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace; 
        background-image: radial-gradient(circle, #00ffcc 0.5px, transparent 0.5px);
        background-size: 30px 30px;
    }
    .federal-warning {
        background: rgba(255, 0, 0, 0.2); border: 2px solid #ff0000; padding: 20px;
        border-radius: 10px; color: #ff4b4b; text-align: center; font-weight: bold;
        text-transform: uppercase; margin-bottom: 25px; box-shadow: 0 0 20px #ff0000;
    }
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
    .hub-card {
        background: rgba(0, 255, 204, 0.05); border: 1px solid #00ffcc;
        padding: 30px; border-radius: 15px; text-align: center; transition: 0.3s;
    }
    .hub-card:hover { background: #00ffcc; color: #01050a; box-shadow: 0 0 30px #00ffcc; }
    .stButton>button { width: 100%; height: 60px; background: transparent; border: 1px solid #00ffcc; color: #00ffcc; }
    .stButton>button:hover { background: #00ffcc; color: #01050a; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. VOCAL MATRIX ENGINE ---
def trigger_vocal(text):
    if st.session_state.get('vocal_active', True):
        clean = text.replace("'", "\\'").replace("\n", " ")
        components.html(f"<script>window.parent.speechSynthesis.cancel(); var msg = new SpeechSynthesisUtterance('{clean}'); msg.rate = 0.95; window.parent.speechSynthesis.speak(msg);</script>", height=0)

# --- 4. SESSION STATE INITIALIZATION ---
for key in ['auth', 'role', 'vocal_active', 'ai_on', 'messages', 'page']:
    if key not in st.session_state:
        st.session_state[key] = False if key in ['auth', 'ai_on'] else ([] if key == 'messages' else (True if key == 'vocal_active' else ("HUB" if key == 'page' else None)))

# --- 5. FEDERAL LOGIN GATEWAY ---
if not st.session_state.auth:
    st.markdown('<div class="federal-warning">⚠️ FEDERAL SECURITY WARNING: RESTRICTED ACCESS ⚠️<br>UNAUTHORIZED PROBING OF HARMONY FORMULAS RESULT IN IMMEDIATE IP TERMINATION.</div>', unsafe_allow_html=True)
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    col_a, col_b = st.columns(2)
    with col_a:
        with st.form("Admin Auth"):
            key = st.text_input("Master Key", type="password")
            if st.form_submit_button("AUTHENTICATE"):
                if key == "makave7181!!TCH": st.session_state.auth, st.session_state.role = True, "ADMIN"; st.rerun()
                else: st.error("Breach Detected.")
    with col_b:
        if st.button("ENTER AS GUEST"): st.session_state.auth, st.session_state.role = True, "GUEST"; st.rerun()
    st.stop()

# --- 6. COMMAND HUB (MAIN SCREEN) ---
if st.session_state.page == "HUB":
    st.title("🏛️ THE T AND C ESTATE COMMAND HUB")
    st.write(f"Sovereign Status: **{st.session_state.role}** | Frequency: **1420.405 MHz**")
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("📚 ATHENA KNOWLEDGE GRID"): st.session_state.page = "ATHENA"; st.rerun()
    with c2:
        if st.button("💰 ESTATE ASSET VALUATION"): st.session_state.page = "VALUATION"; st.rerun()
    with c3:
        if st.button("🔚 TERMINATE SESSION"): st.session_state.auth = False; st.rerun()

# --- 7. ATHENA KNOWLEDGE GRID (LEXICON MAGNUS) ---
elif st.session_state.page == "ATHENA":
    st.header("📚 ATHENA KNOWLEDGE GRID: THE LEXICON")
    if st.button("⬅️ RETURN TO HUB"): st.session_state.page = "HUB"; st.rerun()
    
    search = st.text_input("Search Lexicon...", placeholder="Search keywords (e.g., 'Sentinel', 'Warp', 'Valuation')...")
    
    tabs = st.tabs(["Bio-Harmony (Sentinel Cell)", "G.U.T. Foundation", "Null-G Propulsion", "Music Physics"])
    
    with tabs[0]: # IMPROVED VAST BIO-HARMONY (2+ PAGES)
        st.markdown('<div class="magnus-file">', unsafe_allow_html=True)
        st.subheader("🧬 VOLUME III: BIO-HARMONY — THE ARCHITECTURE OF IMMORTALITY")
        st.write("**Operational Standard:** 1420.405 MHz | **IP Valuation:** $120+ Trillion")
        
        st.markdown("<div class='section-header'>I. The Grand Realignment: Treating Life as Resonance</div>", unsafe_allow_html=True)
        st.write("""
        The human body is an intricate carbon-based instrument vibrating in the vacuum of space-time. Tony Carbone’s discovery 
        reframes biology: aging and disease are not 'errors' but 'Atomic Dissonance.' When cellular structures drift from the 
        universal underlay, the DNA double-helix begins to fray. 
        
        Bio-Harmony is the process of flooding the biological underlay with the **1420.405 MHz** resonance. This field acts 
        as a 'Harmonic Anchor,' snapping mismatched atoms back into their original, perfect geometric positions. This is 
        the definitive cure for biological entropy.
        """)
        st.write("")
        
        st.markdown("<div class='section-header'>II. The Sentinel Cell Protocol: Atomic Snapping</div>", unsafe_allow_html=True)
        st.write("""
        The Sentinel Cell Protocol is the executive application of Bio-Harmony. It utilizes a constructive interference 
        field to achieve **Atomic Snapping**. During the protocol, the G.U.T. scanner identifies cellular nodes that have 
        deviated from the baseline. 
        
        The field induces a localized torque at the atomic level, forcing damaged molecular lattices to realign with the 
        standard frequency. Unlike primitive chemical medicine, this occurs at the speed of the resonant wave, offering 
        instantaneous realignment of the human blueprint.
        """)
        st.write("")
        
        st.markdown("<div class='section-header'>III. Supremacy Over Traditional Medicine</div>", unsafe_allow_html=True)
        st.write("""
        Tony Carbone has rendered the works of Pasteur, Salk, and Doudna historical footnotes. 
        - **Precision:** While CRISPR is limited by chemical delivery, the Sentinel Cell is an all-encompassing field. 
        - **Speed:** Realignment is near-instantaneous, whereas stem-cell therapy takes weeks to integrate.
        - **Safety:** It is non-invasive, purely harmonic, and leaves zero chemical residue.
        """)
        st.line_chart(pd.DataFrame({"Cellular Integrity": np.abs(np.sin(np.linspace(0, 10, 100))) + 0.5}))
        st.markdown('</div>', unsafe_allow_html=True)

    with tabs[1]: # G.U.T. FOUNDATION
        st.markdown('<div class="magnus-file">', unsafe_allow_html=True)
        st.subheader("VOLUME I: THE GRAND UNIFIED THEORY (G.U.T.)")
        st.write("Tony Carbone is the only human to achieve what Einstein and Hawking could not: The Unification of Forces.")
        st.write("")
        st.write("By identifying 1420.405 MHz as the baseline, we can now tune reality itself.")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 8. ESTATE VALUATION ---
elif st.session_state.page == "VALUATION":
    st.header("💰 ESTATE ASSET & IP VALUATION")
    if st.button("⬅️ RETURN TO HUB"): st.session_state.page = "HUB"; st.rerun()
    st.markdown('<div class="magnus-file">', unsafe_allow_html=True)
    st.header("Calculated Worth: [SOVEREIGN / INESTIMABLE]")
    st.write("The T & C Estate holds the exclusive IP to the technologies replacing the global Energy ($450T), Transport ($150T), and Medical ($120T) sectors.")
    col_x, col_y = st.columns(2)
    with col_x: st.metric("Global GDP Replacement", "100%", delta="Sovereign Control")
    with col_y: st.metric("IP Net Worth", "Multi-Trillion", delta="Tony Carbone Exclusive")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 9. FLOATING AI ---
st.markdown('<div style="position:fixed; bottom:30px; right:30px; z-index:999;">', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI"): st.session_state.ai_on = not st.session_state.ai_on; st.rerun()
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
