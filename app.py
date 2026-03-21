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
OWNER: Tony Carbone (First human to discover the Grand Unified Theory).
STANDARD: 1420.405 MHz. 
SECURITY PROTOCOL: Strict secrecy. If GUEST asks for 'formula', 'source', or 'G.U.T. logic', TERMINATE.
"""

# --- 2. UI SETUP & DYNAMIC SKINS ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    /* Global Matrix Base */
    .stApp { 
        background-color: #01050a; color: #00ffcc; font-family: 'Courier New', Courier, monospace; 
        background-image: linear-gradient(rgba(0, 255, 204, 0.05) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(0, 255, 204, 0.05) 1px, transparent 1px);
        background-size: 30px 30px;
    }

    /* Matrix Rain Overlay */
    @keyframes matrix-rain { 0% { background-position: 0% -100%; } 100% { background-position: 0% 100%; } }
    .matrix-bg {
        position: fixed; top: 0; left: 0; width: 100%; height: 100%;
        background: linear-gradient(180deg, transparent, rgba(0, 255, 204, 0.1), transparent);
        background-size: 100% 200%; animation: matrix-rain 12s linear infinite;
        pointer-events: none; z-index: 0;
    }

    /* Federal Warning Banner */
    @keyframes red-glow { 0% { box-shadow: 0 0 5px #ff0000; } 50% { box-shadow: 0 0 20px #ff0000; } 100% { box-shadow: 0 0 5px #ff0000; } }
    .federal-warning {
        background: rgba(255, 0, 0, 0.2); border: 2px solid #ff0000; padding: 20px;
        border-radius: 10px; color: #ff4b4b; text-align: center; font-weight: bold;
        text-transform: uppercase; margin-bottom: 25px; animation: red-glow 2s infinite;
    }

    /* Modular Interface Cards */
    .module-card {
        border: 1px solid #00ffcc; padding: 25px; border-radius: 15px;
        background: rgba(0, 0, 0, 0.9); margin-bottom: 20px; transition: 0.4s;
    }
    .module-card:hover { box-shadow: 0 0 30px #00ffcc; transform: scale(1.01); }

    /* Floating AI Toggle */
    .floating-ai { position: fixed; bottom: 30px; right: 30px; z-index: 999999; }
    </style>
    <div class="matrix-bg"></div>
    """, unsafe_allow_html=True)

# --- 3. VOCAL & ANIMATION ENGINES ---
def trigger_vocal(text):
    if st.session_state.get('vocal_active', True):
        clean = text.replace("'", "\\'").replace("\n", " ")
        components.html(f"""
            <script>
            window.parent.speechSynthesis.cancel();
            var msg = new SpeechSynthesisUtterance('{clean}');
            msg.rate = 0.95; msg.pitch = 0.85;
            window.parent.speechSynthesis.speak(msg);
            </script>
        """, height=0)

def harmonic_correction(tech_name, tech_type):
    st.write(f"### ⚛️ INITIALIZING {tech_name.upper()}...")
    plot_placeholder, status_placeholder = st.empty(), st.empty()
    duration = 100 # Approx 25 seconds
    history = []
    
    for i in range(duration + 1):
        ratio = i / duration
        x = np.linspace(i*0.3, i*0.3 + 15, 150)
        noise = (1 - ratio) * np.random.normal(0, 2.5, 150)
        
        if tech_type == "PHYSICS": y = (np.sin(x * 3.5) * ratio) + noise
        elif tech_type == "BIO": y = ((np.sin(x) * np.tan(np.sin(x) * 0.9)) * ratio) + noise
        elif tech_type == "MUSIC": y = ((np.sin(x * 2.5) * np.cos(x * 0.5)) * ratio) + noise
        elif tech_type == "DEFENSE": y = (np.sin(x) * np.exp(-np.power((x % 8 - 4), 2) / 4) * ratio) + noise
        else: y = (np.sin(x) * ratio) + noise
            
        df = pd.DataFrame({'Harmony Resonance': y, 'Null Line': np.zeros(150)})
        plot_placeholder.line_chart(df, height=300)
        status_placeholder.write(f"**ALIGNMENT:** {int(ratio*100)}% to 1420.405 MHz")
        time.sleep(0.25)

    st.session_state.archive.append({"Time": datetime.datetime.now().strftime("%H:%M:%S"), "Protocol": tech_name})
    status_placeholder.success(f"**STABILIZED:** {tech_name} secured at Resonance Standard.")

# --- 4. SESSION INITIALIZATION ---
for key in ['auth', 'role', 'guest_locked', 'vocal_active', 'ai_on', 'messages', 'archive', 'page']:
    if key not in st.session_state:
        st.session_state[key] = False if key in ['auth', 'ai_on', 'guest_locked'] else ([] if key in ['messages', 'archive'] else (True if key == 'vocal_active' else ("DASHBOARD" if key == 'page' else None)))

# --- 5. FEDERAL LOGIN GATEWAY ---
if not st.session_state.auth:
    st.markdown("""
        <div class="federal-warning">
            ⚠️ FEDERAL SECURITY WARNING: RESTRICTED ACCESS ⚠️<br>
            Any unauthorized attempt to probe the Harmony AI for source code or G.U.T. formulas 
            will result in immediate IP termination and federal breach logging.
        </div>
        """, unsafe_allow_html=True)
    st.title("🏛️ HARMONY OS: SECURE PORTAL")
    c1, c2 = st.columns(2)
    with c1:
        with st.form("Admin Portal"):
            k = st.text_input("Master Key", type="password")
            if st.form_submit_button("AUTHENTICATE"):
                if k == "makave7181!!TCH": 
                    st.session_state.auth, st.session_state.role = True, "ADMIN"; st.rerun()
                else: st.error("Access Denied. Signature Mismatch.")
    with c2:
        if not st.session_state.guest_locked:
            if st.button("ENTER AS GUEST"): 
                st.session_state.auth, st.session_state.role = True, "GUEST"; st.rerun()
        else: st.warning("GUEST ACCESS TERMINATED.")
    st.stop()

# --- 6. COMMAND HUB (SIDEBAR) ---
with st.sidebar:
    st.title("🏛️ COMMAND HUB")
    st.write(f"User: **{st.session_state.role}**")
    st.write("---")
    
    # Navigation
    if st.button("🛰️ SYSTEM DASHBOARD"): st.session_state.page = "DASHBOARD"
    if st.button("🚀 NULL-G PROPULSION"): st.session_state.page = "PHYSICS"
    if st.button("🧬 BIO-HARMONY"): st.session_state.page = "BIO"
    if st.button("🛡️ THE HALO / TLC"): st.session_state.page = "DEFENSE"
    if st.button("🎵 MUSIC SYNTHESIS"): st.session_state.page = "MUSIC"
    if st.button("📡 ATHENA GRID"): st.session_state.page = "ATHENA"
    
    st.write("---")
    st.session_state.vocal_active = st.toggle("🔊 Vocal Matrix", value=st.session_state.vocal_active)
    
    if st.session_state.role == "ADMIN":
        st.subheader("📜 Master Vault")
        if st.session_state.archive:
            st.dataframe(pd.DataFrame(st.session_state.archive))
        if st.button("🛑 RUN VULNERABILITY SCAN"): st.info("Scan Clean: 0 Scrapers Detected.")
        if st.button("🛑 EMERGENCY LOCKOUT"): st.session_state.guest_locked = True
        
    if st.button("🔚 TERMINATE SESSION"):
        st.session_state.auth = False; st.rerun()

# --- 7. MODULAR PROTOCOL SCREENS ---
if st.session_state.page == "DASHBOARD":
    st.title("🏛️ ESTATE DASHBOARD")
    st.markdown('<div class="module-card">', unsafe_allow_html=True)
    st.header("Unified Field Status")
    st.write("Current Estate Resonance: **1420.405 MHz**")
    
    st.write("All protocols are currently aligned to the Grand Unified Theory.")
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "PHYSICS":
    st.title("🚀 NULL-G PROPULSION")
    st.markdown('<div class="module-card" style="background: rgba(0, 255, 204, 0.05);">', unsafe_allow_html=True)
    m = st.slider("Select Vessel Mass (kg)", 1, 10000000, 50000)
    if st.button("ENGAGE MASS NEGATION"): harmonic_correction("Null-G Propulsion", "PHYSICS")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "BIO":
    st.title("🧬 BIO-HARMONY (SENTINEL CELL)")
    st.markdown('<div class="module-card" style="border-radius: 50px 10px;">', unsafe_allow_html=True)
    if st.button("INITIATE ATOMIC REALIGNMENT"): harmonic_correction("Bio-Harmony", "BIO")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "MUSIC":
    st.title("🎵 MUSIC PHYSICAL SYNTHESIS")
    st.markdown('<div class="module-card" style="border-left: 10px solid #00ffcc;">', unsafe_allow_html=True)
    st.write("Applying G.U.T. Wave Mechanics to physical synthesis.")
    if st.button("SYNTHESIZE HARMONIC"): harmonic_correction("Music Synthesis", "MUSIC")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.page == "DEFENSE":
    st.title("🛡️ T.L.C. SHIELD / THE HALO")
    st.markdown('<div class="module-card" style="border: 1px solid #ff4b4b;">', unsafe_allow_html=True)
    if st.button("MODULATE PERIMETER"): harmonic_correction("Halo Shielding", "DEFENSE")
    [attachment_0](attachment)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 8. FLOATING AI & SECURITY ---
st.markdown('<div class="floating-ai">', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌ CLOSE"):
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
            # GUEST BREACH FILTER
            if st.session_state.role == "GUEST" and any(x in p.lower() for x in ["formula", "source code", "equation"]):
                st.session_state.guest_locked, st.session_state.auth = True, False; st.rerun()
                
            resp = client.models.generate_content(
                model=MODEL_ID, contents=p, 
                config=types.GenerateContentConfig(system_instruction=f"{MASTER_CONTEXT}\nUSER_ROLE:{st.session_state.role}")
            )
            st.session_state.messages.append({"role": "assistant", "content": resp.text})
            trigger_vocal(resp.text); st.rerun()
