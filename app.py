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
    </style>
    """, unsafe_allow_html=True)

# --- 3. ACCESS CONTROL (LOGIN SYSTEM) ---
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False
if "user_role" not in st.session_state:
    st.session_state.user_role = None

def login():
    st.title("🏛️ HARMONY OS: SECURE ACCESS")
    with st.container():
        user_input = st.text_input("User Identity")
        pass_input = st.text_input("Access Key", type="password")
        
        if st.button("AUTHENTICATE"):
            # ADMIN CHECK (Tony Carbone)
            if pass_input == "makave7181!!TCH":
                st.session_state.authenticated = True
                st.session_state.user_role = "ADMIN"
                st.rerun()
            # STANDARD USER CHECK (Example: Family/Staff)
            elif pass_input == "Harmony2026":
                st.session_state.authenticated = True
                st.session_state.user_role = "USER"
                st.rerun()
            else:
                st.error("Invalid Credentials. Access Denied.")

if not st.session_state.authenticated:
    login()
    st.stop()

# --- 4. INITIALIZE SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "ai_on" not in st.session_state:
    st.session_state.ai_on = False

# --- 5. SIDEBAR: ADMIN CONSOLE vs USER VIEW ---
with st.sidebar:
    st.title(f"🏛️ {st.session_state.user_role} CONSOLE")
    st.write(f"Active User: {st.session_state.user_role}")
    
    if st.session_state.user_role == "ADMIN":
        st.subheader("Vault Management")
        if st.session_state.messages:
            # Selective Deletion for Admin
            options = [f"{i}: {m['content'][:25]}..." for i, m in enumerate(st.session_state.messages) if m['role'] == 'user']
            to_delete = st.multiselect("Select entries to remove:", options)
            if st.button("Delete Selected"):
                indices = [int(s.split(":")[0]) for s in to_delete]
                for idx in sorted(indices, reverse=True):
                    if idx + 1 < len(st.session_state.messages): st.session_state.messages.pop(idx + 1)
                    st.session_state.messages.pop(idx)
                st.rerun()

            # Master Archive Export
            chat_data = json.dumps(st.session_state.messages, indent=2)
            st.download_button("💾 EXPORT MASTER ARCHIVE", data=chat_data, file_name="harmony_master_vault.json")
        
        if st.button("⚠️ GLOBAL SYSTEM PURGE"):
            st.session_state.messages = []
            st.rerun()
    else:
        st.info("Standard access granted. Vault management restricted to Admin.")

    if st.button("LOGOUT"):
        st.session_state.authenticated = False
        st.session_state.user_role = None
        st.rerun()

# --- 6. API HANDSHAKE & APP ENGINE ---
if "GEMINI_API_KEY" in st.secrets:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    MODEL_ID = "gemini-3.1-flash-lite-preview"
else:
    st.error("🔑 API Link Error"); st.stop()

st.title("🏛️ THE T AND C ESTATE")
st.subheader(f"Harmony OS Suite - {st.session_state.user_role} Mode")

# Application Tabs
app_tabs = st.tabs(["🚀 Null-G", "❄️ Stasis", "🧬 Bio-Harmony", "🛡️ Halo", "🛠️ Diagnostics"])

with app_tabs[0]:
    st.header("Null-G Propulsion")
    m_in = st.number_input("Mass (kg)", value=50000)
    if st.button("ENGAGE"): st.metric("Effective Mass", f"{m_in * 1e-8:.8f} kg")

with app_tabs[1]:
    st.header("Pyro-Stasis")
    if st.button("ACTIVATE STASIS"): st.success("Thermal suspension active. 1420.405 MHz Locked.")

with app_tabs[2]:
    st.header("Bio-Harmony / Sentinel")
    if st.button("SCAN RESONANCE"): st.info("Harmonic Alignment: 100%")

with app_tabs[3]:
    st.header("The Halo")
    if st.button("INITIATE PERIMETER"): st.warning("Halo Shield Online.")

with app_tabs[4]:
    st.header("Diagnostics")
    st.line_chart(1420.405 + 0.005 * np.sin(np.linspace(0, 10, 100)))

# --- 7. FLOATING TOGGLE & CHAT ---
st.markdown('<div class="floating-anchor"></div>', unsafe_allow_html=True)
if st.button("🛰️ HARMONY AI" if not st.session_state.ai_on else "❌ CLOSE AI"):
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
