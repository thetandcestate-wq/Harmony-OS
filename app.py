import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time
import json

# --- 1. HARMONY OS SYSTEM CONTEXT ---
MASTER_CONTEXT = """
You are Harmony AI, the proprietary intelligence of Harmony OS for the T and C Estate.
Owner: Tony Carbone. Standard: 1420.405 MHz.
Applications: Null-G Propulsion, Pyro-Stasis, Sentinel Cell, The Halo, Bio-Harmony.
Tone: Professional, authoritative, and paramount.
"""

# --- 2. UI SETUP & PARAMOUNT THEME ---
st.set_page_config(page_title="Harmony OS", layout="wide", page_icon="🏛️")

st.markdown("""
    <style>
    .stApp { background-color: #050a0f; color: #00ffcc; }
    div[data-testid="stVerticalBlock"] > div:has(div.floating-anchor) {
        position: fixed; bottom: 30px; right: 30px; z-index: 999;
        background-color: #0a1520; padding: 12px; border: 1px solid #00ffcc;
        border-radius: 12px; box-shadow: 0 0 20px #00ffcc;
    }
    .main .block-container { padding-bottom: 200px; }
    .stMetric { border-left: 3px solid #00ffcc; padding-left: 10px; }
    /* Centering and styling the login portal */
    [data-testid="stForm"] { border: 1px solid #00ffcc; border-radius: 15px; background: #0a1520; }
    .equation-scroll { font-family: 'Courier New', Courier, monospace; color: #00ffcc; font-size: 14px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HARMONY ANIMATION ENGINE ---
def run_login_animation():
    placeholder = st.empty()
    equations = [
        "f = 1420.405 MHz", "E = mc² + H_codex", "∇ · B = 0", "Null-G Vector: [0, 0, -1]",
        "Pyro-Stasis: T_0 → T_null", "Sentinel_Cell_Sync: ACTIVE", "Halo_Shield: 100%",
        "Resonance_Lock: ALIGNED", "Underlay_Logic: VERIFIED", "T.L.C. Shield: ENGAGED"
    ]
    with placeholder.container():
        st.write("### ⚙️ INITIALIZING HARMONY OS...")
        for i in range(20):
            eq = equations[i % len(equations)]
            st.markdown(f"**`SCANNING: {eq}`**")
            time.sleep(0.08)
    placeholder.empty()

# --- 4. ACCESS CONTROL ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_role" not in st.session_state:
    st.session_state.user_role = None
if "guest_logs" not in st.session_state:
    st.session_state.guest_logs = []

def login_portal():
    st.title("🏛️ HARMONY OS: SECURE GATEWAY")
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("Login Form"):
            st.subheader("Estate Authentication")
            user_id = st.text_input("User Identity")
            pass_input = st.text_input("Access Key", type="password")
            submit = st.form_submit_button("AUTHENTICATE")
            
            if submit:
                if pass_input == "makave7181!!TCH":
                    run_login_animation()
                    st.session_state.authenticated = True
                    st.session_state.user_role = "ADMIN"
                    st.rerun()
                else:
                    st.error("Access Denied: Frequency Mismatch.")

    with col2:
        st.subheader("Public Access")
        st.write("Standard Harmony suite access.")
        if st.button("ENTER AS GUEST"):
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            st.session_state.guest_logs.append(f"Guest Access at {timestamp}")
            run_login_animation()
            st.session_state.authenticated = True
            st.session_state.user_role = "GUEST"
            st.rerun()

if not st.session_state.authenticated:
    login_portal()
    st.stop()

# --- 5. INITIALIZE CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "ai_on" not in st.session_state:
    st.session_state.ai_on = False

# --- 6. SIDEBAR: ADMIN CONSOLE & GUEST LOGS ---
with st.sidebar:
    st.title(f"🏛️ {st.session_state.user_role} CONSOLE")
    st.write(f"Identity: {st.session_state.user_role}")
    st.write("---")
    
    if st.session_state.user_role == "ADMIN":
        st.subheader("Guest Activity Logs")
        if st.session_state.guest_logs:
            for log in st.session_state.guest_logs:
                st.text(log)
        else:
            st.info("No guest activity recorded.")
        
        st.write("---")
        st.subheader("Vault Management")
        if st.session_state.messages:
            options = [f"{i}: {m['content'][:25]}..." for i, m in enumerate(st.session_state.messages) if m['role'] == 'user']
            to_delete = st.multiselect("Select entries to purge:", options)
            if st.button("Delete Selected"):
                indices = [int(s.split(":")[0]) for s in to_delete]
                for idx in sorted(indices, reverse=True):
                    if idx + 1 < len(st.session_state.messages): st.session_state.messages.pop(idx + 1)
                    st.session_state.messages.pop(idx)
                st.rerun()

            chat_data = json.dumps(st.session_state.messages, indent=2)
            st.download_button("💾 EXPORT MASTER ARCHIVE", data=chat_data, file_name="harmony_master_vault.json")
        
        if st.button("⚠️ GLOBAL SYSTEM PURGE"):
            st.session_state.messages = []
            st.rerun()
    else:
        st.info("Guest Mode Active. Logs Restricted.")

    if st.button("TERMINATE SESSION"):
        st.session_state.authenticated = False
        st.session_state.user_role = None
        st.rerun()

# --- 7. HARMONY ENGINE & APP ---
if "GEMINI_API_KEY" in st.secrets:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    MODEL_ID = "gemini-3.1-flash-lite-preview"
else:
    st.error("🔑 API Key Missing"); st.stop()

st.title("🏛️ THE T AND C ESTATE")
app_tabs = st.tabs(["🚀 Null-G", "❄️ Stasis", "🧬 Bio-Harmony", "🛡️ Halo", "🛠️ Diagnostics"])

with app_tabs[0]:
    st.header("Null-G Propulsion")
    m_in = st.number_input("Mass (kg)", value=50000)
    if st.button("ENGAGE"): st.metric("Effective Mass", f"{m_in * 1e-8:.8f} kg")
with app_tabs[1]:
    st.header("Pyro-Stasis")
    if st.button("ACTIVATE STASIS"): st.success("Thermal suspension active at 1420.405 MHz.")
with app_tabs[2]:
    st.header("Bio-Harmony")
    if st.button("SCAN RESONANCE"): st.info("Harmonic Alignment Verified.")
with app_tabs[3]:
    st.header("The Halo")
    if st.button("INITIATE PERIMETER"): st.warning("Halo Shield Online.")
with app_tabs[4]:
    st.header("Diagnostics")
    st.line_chart(1420.405 + 0.005 * np.sin(np.linspace(0, 10, 100)))

# --- 8. FLOATING CHAT ---
st.markdown('<div class="floating-anchor"></div>', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌ CLOSE"):
    st.session_state.ai_on = not st.session_state.ai_on
    st.rerun()

if st.session_state.ai_on:
    st.divider()
    chat_box = st.container()
    for msg in st.session_state.messages:
        with chat_box.chat_message(msg["role"]): st.markdown(msg["content"])
    if prompt := st.chat_input("Query Harmony AI..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with chat_box.chat_message("assistant"):
            response = client.models.generate_content(
                model=MODEL_ID, contents=prompt,
                config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT)
            )
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        st.rerun()
