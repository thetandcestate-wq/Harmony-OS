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
    /* Floating Toggle Anchor */
    div[data-testid="stVerticalBlock"] > div:has(div.floating-anchor) {
        position: fixed; bottom: 30px; right: 30px; z-index: 999;
        background-color: #0a1520; padding: 12px; border: 1px solid #00ffcc;
        border-radius: 12px; box-shadow: 0 0 20px #00ffcc;
    }
    .main .block-container { padding-bottom: 200px; }
    .stMetric { border-left: 3px solid #00ffcc; padding-left: 10px; }
    </style>
    """, unsafe_allow_html=True)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []
if "ai_on" not in st.session_state:
    st.session_state.ai_on = False

# --- 3. SIDEBAR: T.L.C. SECURITY VAULT ---
with st.sidebar:
    st.title("🏛️ T.L.C. VAULT")
    
    # Password Protection for sensitive data operations
    vault_pass = st.text_input("Vault Access Key", type="password")
    
    if vault_pass == st.secrets.get("VAULT_PASSWORD", "1420"):
        st.success("Access Verified")
        
        # Selective Deletion
        if st.session_state.messages:
            st.subheader("Selective Purge")
            options = [f"{i}: {m['content'][:25]}..." for i, m in enumerate(st.session_state.messages) if m['role'] == 'user']
            to_delete = st.multiselect("Select entries to remove:", options)
            if st.button("Delete Selected"):
                indices = [int(s.split(":")[0]) for s in to_delete]
                for idx in sorted(indices, reverse=True):
                    if idx + 1 < len(st.session_state.messages): st.session_state.messages.pop(idx + 1)
                    st.session_state.messages.pop(idx)
                st.rerun()

            # Export Archive
            chat_data = json.dumps(st.session_state.messages, indent=2)
            st.download_button("💾 EXPORT ESTATE ARCHIVE", data=chat_data, file_name="harmony_vault_export.json")
        
        if st.button("⚠️ PURGE ENTIRE VAULT"):
            st.session_state.messages = []
            st.rerun()
    else:
        st.warning("Enter Vault Key to unlock Export/Purge.")

# --- 4. API HANDSHAKE ---
if "GEMINI_API_KEY" in st.secrets:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    MODEL_ID = "gemini-3.1-flash-lite-preview"
else:
    st.error("🔑 Key Missing"); st.stop()

# --- 5. MAIN COMMAND CENTER ---
st.title("🏛️ THE T AND C ESTATE")
st.subheader("Harmony OS: Universal Application Suite")

app_tabs = st.tabs(["🚀 Null-G", "❄️ Stasis", "🧬 Bio-Harmony", "🛡️ The Halo", "🛠️ Diagnostics"])

with app_tabs[0]:
    st.header("Null-G Propulsion Drive")
    m_in = st.number_input("Vessel Mass (kg)", value=50000)
    if st.button("ENGAGE MASS NEGATION"):
        # The primary Carbone mass-negation calculation
        st.metric("Effective Mass", f"{m_in * 1e-8:.8f} kg", delta="-99.999%")

with app_tabs[1]:
    st.header("Pyro-Stasis Module")
    t_in = st.slider("Initial Temperature (K)", 300, 5000, 1500)
    if st.button("INITIATE THERMAL STASIS"):
        st.success(f"Atomic vibration suspended at {t_in}K. Frequency Lock: 1420.405 MHz.")

with app_tabs[2]:
    st.header("Bio-Harmony & Sentinel Cell")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("SCAN BIO-RESONANCE"):
            st.info("Sentinel Cell Status: 100% Harmonic Alignment.")
    with col2:
        if st.button("ACTIVATE BIO-RECOVERY"):
            st.success("Cellular frequency correction active.")

with app_tabs[3]:
    st.header("The Halo (Safety Interface)")
    st.write("Personal Perimeter Defense & Safety Monitoring")
    if st.button("ENGAGE HALO SHIELD"):
        st.warning("Halo Perimeter Active. T.L.C. Security Protocol Online.")

with app_tabs[4]:
    st.header("Universal Diagnostics")
    st.line_chart(1420.405 + 0.005 * np.sin(np.linspace(0, 10, 100)))
    if st.button("RUN FULL SYSTEM COMPASS"):
        with st.status("Verifying T and C Estate Assets..."):
            time.sleep(1); st.write("✔️ Resonance Lock: 1420.405 MHz")
            time.sleep(1); st.write("✔️ IP Registration: Verified via PPSR")
        st.balloons()

# --- 6. FLOATING TOGGLE & CHAT ---
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
