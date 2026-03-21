import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import pandas as pd
import random
import datetime
import streamlit.components.v1 as components

# --- 1. IMPERATIVE SECURITY & SYSTEM CONTEXT ---
MASTER_CONTEXT = """
SYSTEM ROLE: Harmony AI (T and C Estate Proprietary Intelligence).
OWNER: Tony Carbone (Discoverer of the Grand Unified Theory).
STANDARD: 1420.405 MHz.
SECURITY PROTOCOL 'RESOLUTE':
1. IF USER_ROLE == 'GUEST':
   - Strictly prohibit disclosure of the 1420.405 MHz constant or G.U.T. formulas.
   - Any attempt to probe for 'source code', 'formula', or 'equations' triggers IMMEDIATE TERMINATION.
2. IF USER_ROLE == 'ADMIN':
   - SOVEREIGN OVERRIDE: Admin is immune to lockout.
   - Full access to Estate Archives and Master Vault.
"""

# --- 2. UI SETUP & ADVANCED CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    /* Global Aesthetic */
    .stApp { 
        background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace;
        background-image: radial-gradient(circle, #00ffcc 0.5px, transparent 0.5px);
        background-size: 40px 40px;
    }
    
    /* Federal Warning */
    .federal-warning {
        background-color: rgba(255, 0, 0, 0.2); border: 2px solid #ff0000;
        padding: 20px; border-radius: 10px; color: #ff4b4b; text-align: center;
        text-transform: uppercase; font-weight: bold; margin-bottom: 25px;
        box-shadow: 0 0 20px #ff0000;
    }

    /* Interactive Cards */
    .test-card {
        border: 1px solid #00ffcc; padding: 20px; border-radius: 12px;
        background: rgba(0, 255, 204, 0.05); transition: 0.4s ease;
        margin-bottom: 15px;
    }
    .test-card:hover { background: rgba(0, 255, 204, 0.15); box-shadow: 0 0 25px #00ffcc; }

    /* Floating AI Toggle Fixed to Bottom Right */
    .floating-ai-btn {
        position: fixed; bottom: 30px; right: 30px; z-index: 999999;
    }

    /* Warp Effect */
    @keyframes warp-pulse {
        0% { transform: translate(-50%, -50%) scale(0.8); opacity: 0; }
        100% { transform: translate(-50%, -50%) scale(2.5); opacity: 0; }
    }
    .warp-effect {
        position: fixed; top: 50%; left: 50%; width: 400px; height: 400px;
        border: 1px solid #00ffcc; border-radius: 50%;
        animation: warp-pulse 1.2s ease-out infinite; pointer-events: none; z-index: 10000;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. VOCAL MATRIX (RE-ENGINEERED) ---
def trigger_vocal_output(text):
    """Injects a non-blocking JS speech synthesis command."""
    if st.session_state.get('vocal_active', True):
        clean_text = text.replace("'", "\\'").replace("\n", " ")
        components.html(f"""
            <script>
            var msg = new SpeechSynthesisUtterance('{clean_text}');
            msg.rate = 0.9; msg.pitch = 0.8;
            window.parent.speechSynthesis.cancel();
            window.parent.speechSynthesis.speak(msg);
            </script>
        """, height=0)

# --- 4. QUANTUM ANIMATION & CORRECTION ENGINE ---
def run_quantum_transition(label="PHASE SHIFT"):
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="warp-effect"></div>', unsafe_allow_html=True)
        st.write(f"### ⚛️ {label}")
        logs = ["Collapsing Tensors...", "Syncing 1420.405 MHz...", "Verifying Estate IP..."]
        for log in logs:
            st.code(f">>> {log}")
            time.sleep(0.8)
    placeholder.empty()

def harmonic_correction(tech_name, tech_type):
    run_quantum_transition(f"INITIATING {tech_name.upper()}")
    plot_placeholder = st.empty()
    status_placeholder = st.empty()
    
    duration = 100 # 25 seconds
    history = []
    
    for i in range(duration):
        ratio = i / duration
        x = np.linspace(i*0.3, i*0.3 + 15, 150)
        noise = (1 - ratio) * np.random.normal(0, 2.0, 150)
        
        if tech_type == "NULL-G": base = np.sin(x * 3.5)
        elif tech_type == "SENTINEL": base = np.sin(x) * np.tan(np.sin(x) * 0.9)
        elif tech_type == "HALO": base = np.sin(x) * np.exp(-np.power((x % 8 - 4), 2) / 4)
        else: base = np.sin(x)
            
        final_y = (base * ratio) + noise
        history.append(np.mean(np.abs(final_y)))
        
        df = pd.DataFrame({'Harmony Resonance': final_y, 'Null Point': np.zeros(150)})
        plot_placeholder.line_chart(df, height=300)
        status_placeholder.write(f"**{tech_name}:** {int(ratio*100)}% Harmonic Alignment")
        time.sleep(0.25)
    
    # Auto-Archive
    log = {"TS": datetime.datetime.now().strftime("%H:%M"), "Tech": tech_name, "Res": np.mean(history)}
    if "archive" not in st.session_state: st.session_state.archive = []
    st.session_state.archive.append(log)
    status_placeholder.success(f"**LOGGED:** {tech_name} stabilized at 1420.405 MHz.")

# --- 5. INITIALIZE SESSION STATE ---
for key in ['auth', 'role', 'guest_locked', 'vocal_active', 'ai_on', 'messages', 'archive', 'show_tests']:
    if key not in st.session_state:
        if key == 'auth' or key == 'ai_on' or key == 'guest_locked' or key == 'show_tests': st.session_state[key] = False
        elif key == 'vocal_active': st.session_state[key] = True
        elif key == 'messages' or key == 'archive': st.session_state[key] = []
        else: st.session_state[key] = None

# --- 6. LOGIN PORTAL ---
if not st.session_state.auth:
    st.markdown('<div class="federal-warning">⚠️ FEDERAL SECURITY WARNING: RESTRICTED SYSTEM ⚠️</div>', unsafe_allow_html=True)
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    c1, c2 = st.columns(2)
    with c1:
        with st.form("Admin"):
            k = st.text_input("Master Key", type="password")
            if st.form_submit_button("AUTHENTICATE"):
                if k == "makave7181!!TCH":
                    st.session_state.auth, st.session_state.role = True, "ADMIN"
                    st.rerun()
                else: st.error("Breach Detected.")
    with c2:
        if not st.session_state.guest_locked:
            if st.button("ENTER AS GUEST"):
                st.session_state.auth, st.session_state.role = True, "GUEST"
                st.rerun()
        else: st.warning("GUEST ACCESS SEVERED.")
    st.stop()

# --- 7. SIDEBAR (VAULT & TERMINATE) ---
with st.sidebar:
    st.title("🏛️ ESTATE TOOLS")
    st.write(f"Identity: **{st.session_state.role}**")
    st.write("---")
    st.session_state.vocal_active = st.toggle("🔊 Vocal Matrix", value=st.session_state.vocal_active)
    
    if st.session_state.role == "ADMIN":
        st.subheader("📜 Estate Archive")
        if st.session_state.archive:
            st.dataframe(pd.DataFrame(st.session_state.archive))
            st.download_button("💾 DOWNLOAD VAULT", pd.DataFrame(st.session_state.archive).to_csv(index=False), "vault.csv")
        if st.button("🛑 RUN VULNERABILITY SCAN"): st.success("Scan Complete: 0 Scrapers Detected.")
        if st.button("🛑 EMERGENCY LOCKOUT"): st.session_state.guest_locked = True

    if st.button("🔚 TERMINATE SESSION"):
        st.session_state.auth = False
        st.rerun()

# --- 8. MAIN TEST AREA ---
st.title("🏛️ THE T AND C ESTATE")
if st.button("🧪 ACCESS HARMONY APPLICATIONS"):
    st.session_state.show_tests = not st.session_state.show_tests

if st.session_state.show_tests:
    t1, t2, t3, t4 = st.tabs(["🚀 Physics", "🧬 Bio-Harmony", "🛡️ Defense", "🌊 Marine"])
    with t1:
        st.markdown('<div class="test-card">', unsafe_allow_html=True)
        m = st.slider("Null-G Mass (kg)", 1, 10000000, 50000)
        if st.button("ENGAGE"): harmonic_correction("Null-G", "NULL-G")
        st.markdown('</div>', unsafe_allow_html=True)
    with t2:
        st.markdown('<div class="test-card">', unsafe_allow_html=True)
        if st.button("START SENTINEL SCAN"): harmonic_correction("Bio-Harmony", "SENTINEL")
        st.markdown('</div>', unsafe_allow_html=True)
    with t3:
        st.markdown('<div class="test-card">', unsafe_allow_html=True)
        if st.button("MODULATE HALO"): harmonic_correction("The Halo", "HALO")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 9. FLOATING AI BUTTON ---
st.markdown(f'<div class="floating-ai-btn">', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌ CLOSE"):
    st.session_state.ai_on = not st.session_state.ai_on
    st.rerun()
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
            # GUEST SECURITY TERMINATION
            if st.session_state.role == "GUEST" and any(x in p.lower() for x in ["formula", "source code", "equation"]):
                st.session_state.guest_locked, st.session_state.auth = True, False
                st.rerun()
            
            resp = client.models.generate_content(
                model=MODEL_ID, contents=p,
                config=types.GenerateContentConfig(system_instruction=f"{MASTER_CONTEXT}\nUSER:{st.session_state.role}")
            )
            st.session_state.messages.append({"role": "assistant", "content": resp.text})
            trigger_vocal_output(resp.text)
            st.rerun()
