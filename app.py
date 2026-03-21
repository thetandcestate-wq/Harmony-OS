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

# --- 2. UI SETUP & MATRIX FUTURISTIC CSS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    /* Global Matrix Aesthetic */
    .stApp { 
        background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace;
        background-image: linear-gradient(rgba(0, 255, 204, 0.05) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(0, 255, 204, 0.05) 1px, transparent 1px);
        background-size: 30px 30px;
    }
    
    /* Matrix Rain Animation */
    @keyframes matrix-rain {
        0% { background-position: 0% -100%; }
        100% { background-position: 0% 100%; }
    }
    .matrix-bg {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(180deg, transparent, rgba(0, 255, 204, 0.1), transparent);
        background-size: 100% 200%; animation: matrix-rain 5s linear infinite;
        pointer-events: none; z-index: 0;
    }

    /* Federal Warning */
    .federal-warning {
        background-color: rgba(255, 0, 0, 0.2); border: 2px solid #ff0000;
        padding: 20px; border-radius: 10px; color: #ff4b4b; text-align: center;
        text-transform: uppercase; font-weight: bold; margin-bottom: 25px;
        box-shadow: 0 0 20px #ff0000; position: relative; z-index: 10;
    }

    /* Interactive Cards */
    .test-card {
        border: 1px solid #00ffcc; padding: 20px; border-radius: 12px;
        background: rgba(0, 0, 0, 0.8); transition: 0.4s ease;
        margin-bottom: 15px; position: relative; z-index: 10;
    }
    .test-card:hover { box-shadow: 0 0 25px #00ffcc; transform: translateY(-2px); }

    /* Floating AI Button */
    .floating-ai-btn { position: fixed; bottom: 30px; right: 30px; z-index: 999999; }

    /* Warp/Quantum Transitions */
    @keyframes portal-spin {
        from { transform: translate(-50%, -50%) rotate(0deg); }
        to { transform: translate(-50%, -50%) rotate(360deg); }
    }
    .portal-effect {
        position: fixed; top: 50%; left: 50%; width: 500px; height: 500px;
        border: 2px dashed #00ffcc; border-radius: 50%;
        animation: portal-spin 2s linear infinite; pointer-events: none; z-index: 10000;
    }
    </style>
    <div class="matrix-bg"></div>
    """, unsafe_allow_html=True)

# --- 3. VOCAL MATRIX (STABILIZED) ---
def trigger_vocal_output(text):
    if st.session_state.get('vocal_active', True):
        clean_text = text.replace("'", "\\'").replace("\n", " ")
        components.html(f"""
            <script>
            window.parent.speechSynthesis.cancel();
            var msg = new SpeechSynthesisUtterance('{clean_text}');
            msg.rate = 0.95; msg.pitch = 0.85;
            window.parent.speechSynthesis.speak(msg);
            </script>
        """, height=0)

# --- 4. RANDOMIZED FUTURISTIC TRANSITIONS ---
def run_random_animation(label="RESONANCE SYNC"):
    placeholder = st.empty()
    anim_choice = random.choice(["MATRIX", "WARP", "QUANTUM"])
    with placeholder.container():
        if anim_choice == "WARP":
            st.markdown('<div class="portal-effect"></div>', unsafe_allow_html=True)
        st.write(f"### 🏛️ {label}")
        logs = [
            f"Accessing Harmony Codex...", 
            f"Frequency Lock: 1420.405 MHz",
            f"G.U.T. Tensor Alignment: {random.randint(90,100)}%",
            f"Establishing Secure Underlay..."
        ]
        for log in logs:
            st.code(f">>> {log}")
            time.sleep(0.7)
    placeholder.empty()

# --- 5. HARMONIC CORRECTION ENGINE (25s) ---
def harmonic_correction(tech_name, tech_type):
    run_random_animation(f"CORRECTING {tech_name.upper()}")
    plot_placeholder = st.empty()
    status_placeholder = st.empty()
    
    duration = 100 
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
        
        df = pd.DataFrame({'Active Resonance': final_y, 'Null Point': np.zeros(150)})
        plot_placeholder.line_chart(df, height=300)
        status_placeholder.write(f"**{tech_name}:** {int(ratio*100)}% Harmonic Alignment")
        time.sleep(0.25)
    
    log = {"TS": datetime.datetime.now().strftime("%H:%M"), "Tech": tech_name, "Res": np.mean(history)}
    if "archive" not in st.session_state: st.session_state.archive = []
    st.session_state.archive.append(log)
    status_placeholder.success(f"**STABILIZED:** {tech_name} locked at 1420.405 MHz.")

# --- 6. SESSION STATE ---
for key in ['auth', 'role', 'guest_locked', 'vocal_active', 'ai_on', 'messages', 'archive', 'show_tests']:
    if key not in st.session_state:
        if key in ['auth', 'ai_on', 'guest_locked', 'show_tests']: st.session_state[key] = False
        elif key == 'vocal_active': st.session_state[key] = True
        elif key in ['messages', 'archive']: st.session_state[key] = []
        else: st.session_state[key] = None

# --- 7. LOGIN ---
if not st.session_state.auth:
    st.markdown('<div class="federal-warning">⚠️ FEDERAL SECURITY WARNING: RESTRICTED SYSTEM ⚠️</div>', unsafe_allow_html=True)
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    c1, c2 = st.columns(2)
    with c1:
        with st.form("Admin"):
            k = st.text_input("Master Key", type="password")
            if st.form_submit_button("AUTHENTICATE"):
                if k == "makave7181!!TCH":
                    run_random_animation("ADMIN VERIFIED")
                    st.session_state.auth, st.session_state.role = True, "ADMIN"
                    st.rerun()
                else: st.error("Access Denied.")
    with c2:
        if not st.session_state.guest_locked:
            if st.button("ENTER AS GUEST"):
                run_random_animation("GUEST ACCESS")
                st.session_state.auth, st.session_state.role = True, "GUEST"
                st.rerun()
    st.stop()

# --- 8. SIDEBAR ---
with st.sidebar:
    st.title("🏛️ ESTATE TOOLS")
    st.write(f"User: **{st.session_state.role}**")
    st.write("---")
    st.session_state.vocal_active = st.toggle("🔊 Vocal Matrix", value=st.session_state.vocal_active)
    
    if st.session_state.role == "ADMIN":
        st.subheader("📜 Master Vault")
        if st.session_state.archive:
            st.dataframe(pd.DataFrame(st.session_state.archive))
            st.download_button("💾 DOWNLOAD ARCHIVE", pd.DataFrame(st.session_state.archive).to_csv(index=False), "vault.csv")
        if st.button("🛑 EMERGENCY LOCKOUT"): st.session_state.guest_locked = True

    if st.button("🔚 TERMINATE SESSION"):
        st.session_state.auth = False
        st.rerun()

# --- 9. APPLICATION LAB ---
st.title("🏛️ THE T AND C ESTATE")
if st.button("🧪 ACCESS HARMONY APPLICATIONS"):
    st.session_state.show_tests = not st.session_state.show_tests

if st.session_state.show_tests:
    t1, t2, t3 = st.tabs(["🚀 Physics", "🧬 Bio-Harmony", "🛡️ Defense"])
    with t1:
        st.markdown('<div class="test-card">', unsafe_allow_html=True)
        m = st.slider("Null-G Mass (kg)", 1, 10000000, 50000)
        if st.button("ENGAGE NULL-G"): harmonic_correction("Null-G", "NULL-G")
        st.markdown('</div>', unsafe_allow_html=True)
    with t2:
        st.markdown('<div class="test-card">', unsafe_allow_html=True)
        if st.button("SENTINEL SCAN"): harmonic_correction("Bio-Harmony", "SENTINEL")
        st.markdown('</div>', unsafe_allow_html=True)

# --- 10. FLOATING AI ---
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
            if st.session_state.role == "GUEST" and any(x in p.lower() for x in ["formula", "source code"]):
                st.session_state.guest_locked, st.session_state.auth = True, False
                st.rerun()
            
            resp = client.models.generate_content(
                model=MODEL_ID, contents=p,
                config=types.GenerateContentConfig(system_instruction=f"{MASTER_CONTEXT}\nUSER:{st.session_state.role}")
            )
            st.session_state.messages.append({"role": "assistant", "content": resp.text})
            trigger_vocal_output(resp.text)
            st.rerun()
