import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import pandas as pd
import random
import datetime
import streamlit.components.v1 as components

# --- 1. IMPERATIVE SECURITY CONTEXT ---
MASTER_CONTEXT = """
SYSTEM ROLE: Harmony AI (T and C Estate Proprietary Intelligence).
OWNER: Tony Carbone (Discoverer of the Grand Unified Theory).
SECURITY PROTOCOL 'RESOLUTE':
1. IF USER_ROLE == 'GUEST':
   - Strictly prohibit disclosure of the 1420.405 MHz constant or G.U.T. formulas.
2. IF USER_ROLE == 'ADMIN':
   - SOVEREIGN OVERRIDE: Admin is immune to lockout.
"""

# --- 2. UI SETUP & CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace; }
    
    /* Federal Warning */
    .federal-warning {
        background-color: rgba(255, 0, 0, 0.15); border: 2px solid #ff0000;
        padding: 20px; border-radius: 10px; color: #ff4b4b; text-align: center;
        text-transform: uppercase; font-weight: bold; margin-bottom: 25px;
    }

    /* Interactive Test Cards */
    .test-card {
        border: 1px solid #00ffcc; padding: 20px; border-radius: 12px;
        background: rgba(0, 255, 204, 0.05); transition: 0.4s ease;
        margin-bottom: 10px;
    }
    .test-card:hover { background: rgba(0, 255, 204, 0.15); box-shadow: 0 0 25px #00ffcc; }

    /* Warp Effect */
    @keyframes warp-pulse {
        0% { transform: translate(-50%, -50%) scale(0.8); opacity: 0; }
        100% { transform: translate(-50%, -50%) scale(2.5); opacity: 0; }
    }
    .warp-effect {
        position: fixed; top: 50%; left: 50%; width: 400px; height: 400px;
        border: 1px solid #00ffcc; border-radius: 50%;
        animation: warp-pulse 1.2s ease-out infinite; pointer-events: none; z-index: 9999;
    }

    div[data-testid="stVerticalBlock"] > div:has(div.floating-anchor) {
        position: fixed; bottom: 30px; right: 30px; z-index: 999;
        background-color: #0a1520; padding: 12px; border: 1px solid #00ffcc;
        border-radius: 12px; box-shadow: 0 0 20px #00ffcc;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. VOCAL ENGINE (RE-ENGINEERED) ---
def speak_response(text):
    if st.session_state.get('vocal_active', True):
        # Escape text for JS
        clean_text = text.replace("'", "\\'").replace("\n", " ")
        components.html(f"""
            <script>
            window.parent.speechSynthesis.cancel();
            var msg = new SpeechSynthesisUtterance('{clean_text}');
            msg.rate = 0.9;
            msg.pitch = 0.8;
            window.parent.speechSynthesis.speak(msg);
            </script>
        """, height=0)

# --- 4. QUANTUM TRANSITION ENGINE ---
def run_quantum_transition(label="PHASE SHIFT"):
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="warp-effect"></div>', unsafe_allow_html=True)
        st.write(f"### ⚛️ {label}")
        for log in ["Synchronizing G.U.T. Constants...", "Resonance Lock: 1420.405 MHz"]:
            st.code(f">>> {log}")
            time.sleep(0.8)
    placeholder.empty()

# --- 5. CORRECTION MONITOR (25s) ---
def correction_monitor(tech_name, tech_type):
    run_quantum_transition(f"INITIATING {tech_name.upper()}")
    plot_placeholder, status_placeholder = st.empty(), st.empty()
    duration = 100 
    for i in range(duration):
        ratio = i / duration
        x = np.linspace(i*0.3, i*0.3 + 15, 150)
        noise = (1 - ratio) * np.random.normal(0, 2.0, 150)
        
        if tech_type == "NULL-G": base = np.sin(x * 3.5)
        elif tech_type == "SENTINEL": base = np.sin(x) * np.tan(np.sin(x) * 0.9)
        elif tech_type == "HALO": base = np.sin(x) * np.exp(-np.power((x % 8 - 4), 2) / 4)
        else: base = np.sin(x)
            
        final_y = (base * ratio) + noise
        df = pd.DataFrame({'Active Resonance': final_y, 'Null Point': np.zeros(150)})
        plot_placeholder.line_chart(df, height=300)
        status_placeholder.write(f"**{tech_name}:** {int(ratio*100)}% Harmonic Alignment")
        time.sleep(0.25)
    status_placeholder.success(f"**ALIGNED:** {tech_name} stabilized at 1420.405 MHz.")

# --- 6. ACCESS CONTROL ---
if "auth" not in st.session_state: st.session_state.auth, st.session_state.role = False, None
if "guest_locked" not in st.session_state: st.session_state.guest_locked = False
if "vocal_active" not in st.session_state: st.session_state.vocal_active = True
if "messages" not in st.session_state: st.session_state.messages = []

def login_portal():
    st.markdown('<div class="federal-warning">⚠️ FEDERAL SECURITY WARNING: RESTRICTED SYSTEM ⚠️</div>', unsafe_allow_html=True)
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    col1, col2 = st.columns(2)
    with col1:
        with st.form("Admin Auth"):
            key = st.text_input("Master Key", type="password")
            if st.form_submit_button("AUTHENTICATE"):
                if key == "makave7181!!TCH":
                    run_quantum_transition("ADMIN VERIFIED")
                    st.session_state.auth, st.session_state.role = True, "ADMIN"
                    st.rerun()
                else: st.error("Access Denied.")
    with col2:
        if not st.session_state.guest_locked:
            if st.button("ENTER AS GUEST"):
                run_quantum_transition("GUEST ACCESS")
                st.session_state.auth, st.session_state.role = True, "GUEST"
                st.rerun()

if not st.session_state.auth:
    login_portal()
    st.stop()

# --- 7. MAIN INTERFACE ---
st.title("🏛️ THE T AND C ESTATE")

with st.sidebar:
    st.title("🛠️ SYSTEM CONTROLS")
    st.session_state.vocal_active = st.toggle("🔊 Vocal Matrix", value=st.session_state.vocal_active)
    if st.session_state.role == "ADMIN":
        if st.button("🛑 EMERGENCY LOCKOUT"): st.session_state.guest_locked = True
    if st.button("TERMINATE SESSION"):
        st.session_state.auth = False
        st.rerun()

# Restored Test Area
st.write("---")
if st.button("🧪 ACCESS HARMONY APPLICATIONS"):
    st.session_state.show_tests = not st.session_state.get('show_tests', False)

if st.session_state.get('show_tests'):
    tabs = st.tabs(["🚀 Physics", "🧬 Bio-Harmony", "🛡️ Defense"])
    with tabs[0]: 
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="test-card">', unsafe_allow_html=True)
            st.write("### Null-G Drive")
            mass = st.slider("Mass (kg)", 1, 10000000, 50000)
            if st.button("ENGAGE"): correction_monitor("Null-G", "NULL-G")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="test-card">', unsafe_allow_html=True)
            st.write("### Pyro-Stasis")
            if st.button("LOCK ENTROPY"): correction_monitor("Pyro-Stasis", "STASIS")
            st.markdown('</div>', unsafe_allow_html=True)
    with tabs[1]:
        st.markdown('<div class="test-card">', unsafe_allow_html=True)
        st.write("### Bio-Harmony (Sentinel Cell)")
        if st.button("SCAN ATOMS"): correction_monitor("Bio-Harmony", "SENTINEL")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 8. FLOATING CHAT & AI ---
st.markdown('<div class="floating-anchor"></div>', unsafe_allow_html=True)
if "ai_on" not in st.session_state: st.session_state.ai_on = False

if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌"):
    st.session_state.ai_on = not st.session_state.ai_on
    st.rerun()

if st.session_state.ai_on:
    if "GEMINI_API_KEY" in st.secrets:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
        MODEL_ID = "gemini-3.1-flash-lite-preview"
        chat_box = st.container()
        
        for msg in st.session_state.messages:
            with chat_box.chat_message(msg["role"]): st.markdown(msg["content"])
        
        if prompt := st.chat_input("Query Harmony AI..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # Security
            forbidden = ["formula", "equation", "source code"]
            if st.session_state.role == "GUEST" and any(x in prompt.lower() for x in forbidden):
                st.session_state.guest_locked, st.session_state.auth = True, False
                st.rerun()
                
            response = client.models.generate_content(
                model=MODEL_ID, contents=prompt,
                config=types.GenerateContentConfig(system_instruction=f"{MASTER_CONTEXT}\nUSER:{st.session_state.role}")
            )
            
            ai_text = response.text
            st.session_state.messages.append({"role": "assistant", "content": ai_text})
            
            if st.session_state.vocal_active:
                speak_response(ai_text)
                
            st.rerun()
