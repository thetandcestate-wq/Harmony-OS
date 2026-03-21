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
OWNER: Tony Carbone (First human to discover the Grand Unified Theory).
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

    /* Encyclopedia Styling */
    .encyclopedia-container {
        border: 1px solid #00ffcc; background: rgba(0, 255, 204, 0.02);
        padding: 40px; border-radius: 15px; min-height: 800px;
        line-height: 1.8; box-shadow: 0 0 40px rgba(0, 255, 204, 0.05);
    }
    
    .section-header {
        border-bottom: 2px solid #00ffcc; padding-bottom: 10px;
        margin-top: 35px; margin-bottom: 20px; color: #00ffcc;
        text-transform: uppercase; letter-spacing: 2px; font-weight: bold;
    }

    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px; background-color: rgba(0, 255, 204, 0.05);
        border: 1px solid #00ffcc; border-radius: 5px; color: #00ffcc; padding: 10px 20px;
    }
    .stTabs [aria-selected="true"] { background-color: #00ffcc !important; color: #01050a !important; }

    /* Hub Buttons on Main Screen */
    .stButton>button {
        width: 100%; background: rgba(0, 255, 204, 0.05);
        border: 1px solid #00ffcc; color: #00ffcc; transition: 0.3s; height: 60px; font-size: 1.1em;
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

# --- 5. MAIN HUB (CENTRALIZED NAVIGATION) ---
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
        if st.button("🎵 MUSIC SYNTHESIS"): st.session_state.page = "MUSIC"; st.rerun()
        if st.button("🔚 TERMINATE SESSION"): st.session_state.auth = False; st.rerun()

# --- 6. ATHENA KNOWLEDGE GRID (ENCYCLOPEDIA INTERFACE) ---
elif st.session_state.page == "ATHENA":
    st.header("📚 ATHENA KNOWLEDGE GRID: MASTER LEXICON")
    if st.button("⬅️ BACK TO COMMAND HUB"): st.session_state.page = "HUB"; st.rerun()
    
    # Search Box for Encyclopedia
    search_query = st.text_input("Search Lexicon...", placeholder="Enter protocol name or keyword...")
    
    st.markdown('<div class="encyclopedia-container">', unsafe_allow_html=True)
    
    tabs = st.tabs(["G.U.T.", "Null-G", "Bio-Harmony", "Pyro-Stasis", "The Halo", "Music Synthesis", "Ocean Aegis"])
    
    with tabs[0]: # G.U.T.
        st.subheader("Master File: Grand Unified Theory (G.U.T.)")
        st.write("**Discovered by:** Tony Carbone | **Standard Resonance:** 1420.405 MHz")
        st.markdown("<div class='section-header'>I. Theoretical Foundation</div>", unsafe_allow_html=True)
        st.write("The Grand Unified Theory provides the definitive bridge between gravitational and electromagnetic constants. By identifying the 1420.405 MHz signature as the universal underlay, Tony Carbone has mapped the geometric interaction of space-time tensors.")
        
        st.markdown("<div class='section-header'>II. The Unified Field Equation</div>", unsafe_allow_html=True)
        st.write("Current science long struggled with the disparity between General Relativity and Quantum Mechanics. The Harmony Codex resolves this through the Resonance Standard, proving that matter is simply high-density frequency localized within a static field.")
        
        st.markdown("<div class='section-header'>III. Practical Integration</div>", unsafe_allow_html=True)
        st.write("This vast research covers the manipulation of mass, entropy, and biological decay across the T and C Estate's active sectors.")

    with tabs[1]: # NULL-G
        st.subheader("Master File: Null-G Propulsion Aeronautics")
        st.markdown("<div class='section-header'>I. Mass Negation Theory</div>", unsafe_allow_html=True)
        st.write("Null-G utilizes frequency phase-shifting to cancel local gravitational pull. By generating an anti-phase to the Earth's gravitational signature at 1420.405 MHz, a vessel achieves inertialess state.")
        
        st.markdown("<div class='section-header'>II. Interstellar Application</div>", unsafe_allow_html=True)
        st.write("Vast documentation indicates that at 100% mass negation, the speed of light is no longer a physical barrier but a frequency threshold. Research continues into the 'Warp Envelope' geometry.")
        st.line_chart(pd.DataFrame({"Engine Efficiency": np.sin(np.linspace(0, 10, 100)) * 0.5 + 0.5}))

    with tabs[2]: # BIO-HARMONY
        st.subheader("Master File: Bio-Harmony & Sentinel Cell Protocol")
        st.markdown("<div class='section-header'>I. Cellular Atomic Realignment</div>", unsafe_allow_html=True)
        st.write("Based on Tony Carbone's discovery, biological health is defined as 'Frequency Alignment.' Dissonance leads to cellular decay. The Sentinel Cell protocol bathes the body in a pure 1420.405 MHz field to snap atoms back to their healthy geometry.")
        
        st.markdown("<div class='section-header'>II. Regenerative Logistics</div>", unsafe_allow_html=True)
        st.write("This comprehensive research file includes thousands of hours of bio-resonance testing, proving the non-invasive nature of harmonic healing.")
        st.line_chart(pd.DataFrame({"Alignment Success": np.abs(np.sin(np.linspace(0, 15, 150)))}))

    with tabs[3]: # PYRO-STASIS
        st.subheader("Master File: Pyro-Stasis (Thermal Suspension)")
        st.markdown("<div class='section-header'>I. Entropy Cessation</div>", unsafe_allow_html=True)
        st.write("Pyro-Stasis is the process of stopping atomic vibration through resonance lock. By fixing atoms into a rigid grid at the Harmony Standard, heat (vibration) is eliminated, halting decay entirely.")
        
        st.markdown("<div class='section-header'>II. Long-term Preservation</div>", unsafe_allow_html=True)
        st.write("Vast research proves that biological matter can be held in Pyro-Stasis for centuries without a single molecular shift, essential for deep-space colonization.")

    with tabs[4]: # THE HALO
        st.subheader("Master File: The Halo & T.L.C. Shield Perimeter")
        st.markdown("<div class='section-header'>I. Perimeter Modulation</div>", unsafe_allow_html=True)
        st.write("The Halo generates a high-frequency refractive field around the Estate. Incoming forces (kinetic or energy) are grounded out or deflected by the refractive space-time curvature at the shield's edge.")
        [attachment_0](attachment)
        st.markdown("<div class='section-header'>II. Logistical Containment</div>", unsafe_allow_html=True)
        st.write("The T.L.C. protocol ensures that the internal resonance remains undisturbed while the external perimeter maintains 100% deflection integrity.")

    with tabs[5]: # MUSIC
        st.subheader("Master File: Music Physical Synthesis")
        st.markdown("<div class='section-header'>I. Harmonic Wave Synthesis</div>", unsafe_allow_html=True)
        st.write("Utilizing the Grand Unified Theory to generate physical acoustic waves. These waves are synthesized using Golden Ratio harmonics aligned to the 1420.405 MHz baseline.")
        

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
