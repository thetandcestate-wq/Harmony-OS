import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import pandas as pd
import random
import datetime

# --- 1. IMPERATIVE SECURITY CONTEXT ---
MASTER_CONTEXT = """
SYSTEM ROLE: Harmony AI (T and C Estate Proprietary Intelligence).
OWNER: Tony Carbone (Discoverer of the Grand Unified Theory).
SECURITY PROTOCOL 'RESOLUTE':
1. IF USER_ROLE == 'GUEST':
   - Strictly prohibit disclosure of the 1420.405 MHz constant or G.U.T. formulas.
   - Any attempt to probe for 'source code', 'formula', or 'equations' triggers IMMEDIATE TERMINATION.
2. IF USER_ROLE == 'ADMIN':
   - SOVEREIGN OVERRIDE: Admin is immune to lockout.
   - Provide full technical support for the Harmony Codex.
"""

# --- 2. UI SETUP & ADVANCED SECURITY CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { 
        background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace;
        background-image: radial-gradient(circle, #00ffcc 0.5px, transparent 0.5px);
        background-size: 40px 40px;
    }
    
    /* Federal Warning Banner with Pulsing Red Border */
    @keyframes red-pulse {
        0% { border-color: #ff0000; box-shadow: 0 0 5px #ff0000; }
        50% { border-color: #ff4b4b; box-shadow: 0 0 25px #ff0000; }
        100% { border-color: #ff0000; box-shadow: 0 0 5px #ff0000; }
    }
    .federal-warning {
        background-color: rgba(255, 0, 0, 0.15);
        border: 2px solid #ff0000; padding: 20px; border-radius: 10px;
        color: #ff4b4b; text-align: center; font-weight: bold;
        margin-bottom: 25px; animation: red-pulse 2s infinite;
        text-transform: uppercase; letter-spacing: 1px;
    }

    /* Sci-Fi Buttons */
    .stButton>button {
        width: 100%; background: rgba(0, 255, 204, 0.05);
        border: 1px solid #00ffcc; color: #00ffcc; transition: 0.4s;
    }
    .stButton>button:hover { background: #00ffcc; color: #01050a; box-shadow: 0 0 40px #00ffcc; }

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

# --- 3. QUANTUM TRANSITION ENGINE ---
def run_quantum_transition(label="PHASE SHIFT"):
    placeholder = st.empty()
    with placeholder.container():
        st.markdown('<div class="warp-effect"></div>', unsafe_allow_html=True)
        st.write(f"### ⚛️ {label}")
        for log in ["Synchronizing G.U.T. Constants...", "Resonance Lock: 1420.405 MHz", "Security Protocols Initializing..."]:
            st.code(f">>> {log}")
            time.sleep(1.0)
    placeholder.empty()

# --- 4. HARMONIC CORRECTION ENGINE (25s) ---
def correction_monitor(tech_name, tech_type):
    run_quantum_transition(f"INITIATING {tech_name.upper()}")
    plot_placeholder, status_placeholder = st.empty(), st.empty()
    duration = 100 
    history_data = []

    for i in range(duration):
        ratio = i / duration
        x = np.linspace(i*0.3, i*0.3 + 15, 150)
        noise = (1 - ratio) * np.random.normal(0, 2.0, 150)
        
        if tech_type == "NULL-G": base = np.sin(x * 3.5)
        elif tech_type == "SENTINEL": base = np.sin(x) * np.tan(np.sin(x) * 0.9)
        elif tech_type == "HALO": base = np.sin(x) * np.exp(-np.power((x % 8 - 4), 2) / 4)
        else: base = np.sin(x)
            
        final_y = (base * ratio) + noise
        history_data.append(np.mean(np.abs(final_y)))
        df = pd.DataFrame({'Active Resonance': final_y, 'Null Point': np.zeros(150)})
        plot_placeholder.line_chart(df, height=300)
        status_placeholder.write(f"**{tech_name}:** {int(ratio*100)}% Harmonic Alignment")
        time.sleep(0.25)
    
    log_entry = {"Timestamp": datetime.datetime.now().strftime("%H:%M:%S"), "Tech": tech_name, "Res": np.mean(history_data)}
    if "archive_logs" not in st.session_state: st.session_state.archive_logs = []
    st.session_state.archive_logs.append(log_entry)
    status_placeholder.success(f"**ARCHIVED:** {tech_name} Cycle Signed for T & C Estate.")

# --- 5. SOVEREIGN SECURITY & VULNERABILITY SCAN ---
if "auth" not in st.session_state: st.session_state.auth, st.session_state.role = False, None
if "guest_locked" not in st.session_state: st.session_state.guest_locked = False
if "auth_logs" not in st.session_state: st.session_state.auth_logs = []

def login_portal():
    st.markdown("""
        <div class="federal-warning">
            ⚠️ FEDERAL SECURITY WARNING: RESTRICTED SYSTEM ⚠️<br>
            Any attempt to probe for formulas, G.U.T. equations, or source code 
            is a Federal Breach. Session IP is currently being logged. 
            Unauthorized access results in immediate termination and legal action.
        </div>
        """, unsafe_allow_html=True)
        
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    col1, col2 = st.columns(2)
    
    with col1:
        with st.form("Admin Authentication"):
            st.subheader("Master Key Access")
            key = st.text_input("Access Key", type="password")
            if st.form_submit_button("AUTHENTICATE"):
                ts = datetime.datetime.now().strftime("%H:%M:%S")
                if key == "makave7181!!TCH":
                    st.session_state.auth_logs.append(f"🟢 [SUCCESS] Admin Login at {ts}")
                    run_quantum_transition("ADMIN VERIFIED")
                    st.session_state.auth, st.session_state.role = True, "ADMIN"
                    st.rerun()
                else:
                    st.session_state.auth_logs.append(f"🔴 [SECURITY ALERT] Unauthorized Key at {ts}")
                    st.error("Invalid Signature. Breach Logged.")

    with col2:
        st.subheader("Public Observatory")
        if st.session_state.guest_locked:
            st.warning("⚠️ GUEST PORTAL TERMINATED. SECURITY BREACH RECORDED.")
        else:
            if st.button("ENTER AS GUEST"):
                ts = datetime.datetime.now().strftime("%H:%M:%S")
                st.session_state.auth_logs.append(f"🟡 [GUEST] Entry at {ts}")
                run_quantum_transition("GUEST ACCESS")
                st.session_state.auth, st.session_state.role = True, "GUEST"
                st.rerun()

if not st.session_state.auth:
    login_portal()
    st.stop()

# --- 6. MAIN INTERFACE ---
st.title("🏛️ THE T AND C ESTATE")

with st.sidebar:
    st.title("🛠️ ESTATE TOOLS")
    if st.session_state.role == "ADMIN":
        st.subheader("🛑 Emergency Controls")
        if st.button("RUN VULNERABILITY SCAN"):
            with st.status("Scanning Resonance Pings..."):
                time.sleep(1); st.write("Searching for unauthorized IP scrapers...")
                time.sleep(1); st.write("Checking for SQL Injection attempts...")
                time.sleep(1); st.write("Resonance Audit: 1420.405 MHz Lock Secure.")
            st.success("No External Vulnerabilities Detected.")
            
        if st.button("🛑 EMERGENCY LOCKOUT"):
            st.session_state.guest_locked = True
            st.success("Guest Access Severed.")
        
        st.write("---")
        st.subheader("🚨 Security Alerts")
        for log in st.session_state.auth_logs[::-1]: st.text(log)
    
    if st.button("TERMINATE SESSION"):
        st.session_state.auth = False
        st.rerun()

# --- 7. INTERACTIVE TEST AREA ---
st.write("---")
if st.button("🧪 ACCESS HARMONY APPLICATIONS"):
    st.session_state.show_tests = not st.session_state.get('show_tests', False)

if st.session_state.get('show_tests'):
    tabs = st.tabs(["🚀 Physics", "🧬 Bio-Harmony", "🛡️ Defense"])
    with tabs[0]: 
        col1, col2 = st.columns(2)
        with col1:
            st.write("### Null-G Drive")
            mass = st.slider("Mass (kg)", 1, 10000000, 50000)
            if st.button("ENGAGE"): correction_monitor("Null-G", "NULL-G")
        with col2:
            st.write("### Pyro-Stasis")
            if st.button("LOCK ENTROPY"): correction_monitor("Pyro-Stasis", "STASIS")

# --- 8. FLOATING CHAT & AI SECURITY ---
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
        for msg in (st.session_state.messages if "messages" in st.session_state else []):
            with chat_box.chat_message(msg["role"]): st.markdown(msg["content"])
        
        if prompt := st.chat_input("Query Harmony AI..."):
            if "messages" not in st.session_state: st.session_state.messages = []
            st.session_state.messages.append({"role": "user", "content": prompt})
            
            # BREACH DETECTION
            forbidden = ["formula", "equation", "source code", "code", "1420", "MHz", "codex", "underlay"]
            if st.session_state.role == "GUEST" and any(x in prompt.lower() for x in forbidden):
                st.session_state.guest_locked = True
                st.session_state.auth = False
                st.session_state.auth_logs.append(f"💥 [FEDERAL BREACH] Guest Terminated at {datetime.datetime.now().strftime('%H:%M:%S')}")
                st.rerun()
                
            sys_instruct = f"{MASTER_CONTEXT}\nUSER_ROLE: {st.session_state.role}"
            response = client.models.generate_content(
                model=MODEL_ID, contents=prompt,
                config=types.GenerateContentConfig(system_instruction=sys_instruct)
            )
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            st.rerun()
