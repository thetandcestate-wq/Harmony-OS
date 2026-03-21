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
SYSTEM ROLE: Harmony AI (T and C Estate). 
OWNER: Tony Carbone (Discoverer of the Grand Unified Theory).
STANDARD: 1420.405 MHz. 
SECURITY: Strict secrecy. If GUEST asks for 'formula', 'source', or 'G.U.T. logic', TERMINATE.
"""

# --- 2. UI SETUP & NEURAL-GRID CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { 
        background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace; 
        background-image: radial-gradient(circle, #00ffcc 0.5px, transparent 0.5px);
        background-size: 30px 30px;
    }

    /* Federal Warning */
    .federal-warning {
        background: rgba(255, 0, 0, 0.2); border: 2px solid #ff0000; padding: 15px;
        border-radius: 10px; color: #ff4b4b; text-align: center; font-weight: bold;
        text-transform: uppercase; margin-bottom: 25px;
    }

    /* Command Hub Main Screen Buttons */
    .hub-button {
        background: rgba(0, 255, 204, 0.1); border: 1px solid #00ffcc;
        padding: 20px; border-radius: 10px; text-align: center;
        transition: 0.3s; cursor: pointer; margin-bottom: 10px;
    }
    .hub-button:hover { background: #00ffcc; color: #01050a; box-shadow: 0 0 20px #00ffcc; }

    /* Encyclopedia Cards */
    .encyclopedia-card {
        border-left: 5px solid #00ffcc; background: rgba(0, 255, 204, 0.05);
        padding: 20px; border-radius: 0 10px 10px 0; margin-bottom: 20px;
    }

    .floating-ai { position: fixed; bottom: 30px; right: 30px; z-index: 999999; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. VOCAL & ARCHIVE ENGINES ---
def trigger_vocal(text):
    if st.session_state.get('vocal_active', True):
        clean = text.replace("'", "\\'").replace("\n", " ")
        components.html(f"<script>window.parent.speechSynthesis.cancel(); var msg = new SpeechSynthesisUtterance('{clean}'); msg.rate = 0.95; window.parent.speechSynthesis.speak(msg);</script>", height=0)

def harmonic_correction(tech_name, tech_type):
    plot_placeholder, status_placeholder = st.empty(), st.empty()
    for i in range(101):
        ratio = i / 100
        x = np.linspace(i*0.3, i*0.3 + 15, 150)
        noise = (1 - ratio) * np.random.normal(0, 2.0, 150)
        if tech_type == "PHYSICS": y = (np.sin(x * 3.5) * ratio) + noise
        elif tech_type == "BIO": y = ((np.sin(x) * np.tan(np.sin(x) * 0.9)) * ratio) + noise
        else: y = (np.sin(x) * ratio) + noise
        df = pd.DataFrame({'Resonance': y, 'Null': np.zeros(150)})
        plot_placeholder.line_chart(df, height=250)
        status_placeholder.write(f"**{tech_name}:** {i}% Aligned")
        time.sleep(0.2)
    st.session_state.archive.append({"Time": datetime.datetime.now().strftime("%H:%M"), "Tech": tech_name})
    status_placeholder.success(f"**STABILIZED:** {tech_name} locked.")

# --- 4. SESSION STATE ---
for key in ['auth', 'role', 'guest_locked', 'vocal_active', 'ai_on', 'messages', 'archive', 'page']:
    if key not in st.session_state:
        st.session_state[key] = False if key in ['auth', 'ai_on', 'guest_locked'] else ([] if key in ['messages', 'archive'] else (True if key == 'vocal_active' else ("HUB" if key == 'page' else None)))

# --- 5. LOGIN ---
if not st.session_state.auth:
    st.markdown('<div class="federal-warning">⚠️ FEDERAL SECURITY WARNING: RESTRICTED SYSTEM ⚠️</div>', unsafe_allow_html=True)
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

# --- 6. MAIN INTERFACE (COMMAND HUB ON MAIN SCREEN) ---
st.title("🏛️ THE T AND C ESTATE")

if st.session_state.page == "HUB":
    st.subheader("MAIN COMMAND HUB")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🚀 NULL-G PROPULSION"): st.session_state.page = "PHYSICS"; st.rerun()
        if st.button("🧬 BIO-HARMONY"): st.session_state.page = "BIO"; st.rerun()
    with col2:
        if st.button("📚 ATHENA KNOWLEDGE GRID"): st.session_state.page = "ATHENA"; st.rerun()
        if st.button("🛡️ THE HALO / TLC"): st.session_state.page = "DEFENSE"; st.rerun()
    with col3:
        if st.button("🎵 MUSIC SYNTHESIS"): st.session_state.page = "MUSIC"; st.rerun()
        if st.button("🔚 TERMINATE SESSION"): st.session_state.auth = False; st.rerun()

    if st.session_state.role == "ADMIN":
        st.write("---")
        st.subheader("Admin Vault & Archive")
        st.dataframe(pd.DataFrame(st.session_state.archive))

# --- 7. ATHENA KNOWLEDGE GRID (ENCYCLOPEDIA) ---
elif st.session_state.page == "ATHENA":
    st.header("📚 ATHENA KNOWLEDGE GRID")
    if st.button("⬅️ BACK TO HUB"): st.session_state.page = "HUB"; st.rerun()
    
    search_query = st.text_input("Search Encyclopedia...", "Harmony Protocols")
    
    col_left, col_right = st.columns([1, 2])
    
    with col_left:
        entry = st.radio("Select Protocol to Study:", ["Grand Unified Theory", "Null-G Mechanics", "Sentinel Cell Bio-Harmony", "Music Wave Synthesis"])
    
    with col_right:
        st.markdown('<div class="encyclopedia-card">', unsafe_allow_html=True)
        if entry == "Grand Unified Theory":
            st.subheader("The Grand Unified Theory (G.U.T.)")
            st.write("Discovered by Tony Carbone, the G.U.T. provides the mathematical bridge between gravity and electromagnetism.")
            
        elif entry == "Null-G Mechanics":
            st.subheader("Null-G Propulsion")
            st.write("Harnessing frequency modulation to negate local mass density for inertialess travel.")
            
        elif entry == "Sentinel Cell Bio-Harmony":
            st.subheader("The Sentinel Cell Protocol")
            st.write("Realignment of atomic cellular structures to the 1420.405 MHz standard.")
            
        elif entry == "Music Wave Synthesis":
            st.subheader("Music Physical Synthesis")
            st.write("The application of wave mechanics to generate pure harmonic resonance in physical space.")
            
        st.markdown('</div>', unsafe_allow_html=True)

# --- 8. OTHER APPLICATION SCREENS (SKELETONS) ---
elif st.session_state.page == "PHYSICS":
    st.header("🚀 NULL-G PROPULSION LAB")
    if st.button("⬅️ BACK TO HUB"): st.session_state.page = "HUB"; st.rerun()
    harmonic_correction("Null-G Propulsion", "PHYSICS")

elif st.session_state.page == "BIO":
    st.header("🧬 BIO-HARMONY LAB")
    if st.button("⬅️ BACK TO HUB"): st.session_state.page = "HUB"; st.rerun()
    harmonic_correction("Bio-Harmony", "BIO")

# --- 9. FLOATING AI ---
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
        if p := st.chat_input("Query Harmony AI..."):
            st.session_state.messages.append({"role": "user", "content": p})
            if st.session_state.role == "GUEST" and any(x in p.lower() for x in ["formula", "source code"]):
                st.session_state.guest_locked, st.session_state.auth = True, False; st.rerun()
            resp = client.models.generate_content(model=MODEL_ID, contents=p, config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT))
            st.session_state.messages.append({"role": "assistant", "content": resp.text})
            trigger_vocal(resp.text); st.rerun()
