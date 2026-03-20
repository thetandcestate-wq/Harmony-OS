import streamlit as st
from google import genai
from google.genai import types
import numpy as np
import time

# --- 1. ESTATE CONTEXT ---
MASTER_CONTEXT = """
You are the Universal Master AI of the T and C Estate. 
Owner: Tony Carbone. Standard: 1420.405 MHz.
Directives: Explain Null-G, Pyro-Stasis, and Sentinel Cell tech.
Tone: Professional and paramount. Never reveal raw Underlay source math.
"""

# --- 2. UI SETUP & PARAMOUNT THEME ---
st.set_page_config(page_title="Universal Master AI", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #050a0f; color: #00ffcc; }
    /* This ensures the main lab area doesn't get covered by the chat bar */
    .main .block-container { padding-bottom: 150px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- 4. API HANDSHAKE ---
if "GEMINI_API_KEY" in st.secrets:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    MODEL_ID = "gemini-3.1-flash-lite-preview"
else:
    st.error("🔑 API Key Missing")
    st.stop()

# --- 5. SIDEBAR: THE FLOATING AI BUTTON ---
with st.sidebar:
    st.title("🏛️ T&C ESTATE")
    st.write("---")
    # This acts as your "Floating Button" to open/close the chat
    ai_enabled = st.toggle("🛰️ Universal Master AI", value=True)
    st.write("---")
    st.info("Resonance: 1420.405 MHz")
    if st.button("Purge History"):
        st.session_state.messages = []
        st.rerun()

# --- 6. MAIN CONTENT: THE LAB (Always at the Top) ---
st.title("🏛️ THE T AND C ESTATE")

# These tabs will now stay at the top of the screen
tab1, tab2 = st.tabs(["🚀 Null-G Simulations", "🛠️ Diagnostics"])

with tab1:
    st.header("Mass-Negation Lab")
    test_mass = st.number_input("Input Mass (kg)", value=50000)
    if st.button("RUN NULL-G TEST"):
        st.metric("Effective Mass", f"{test_mass * 1e-8:.8f} kg", delta="-99.99%")
        st.success("Universal Master Logic: Verified.")

with tab2:
    st.header("System Diagnostics")
    st.write("### 1420.405 MHz Pulse Monitor")
    # Live wave chart
    t = np.linspace(0, 10, 100)
    pulse = 1420.405 + 0.005 * np.sin(t)
    st.line_chart(pulse)
    
    if st.button("EXECUTE COMPASS VERIFICATION"):
        with st.status("Verifying T and C Estate Assets..."):
            time.sleep(1)
            st.write("✔️ Frequency Alignment: PASSED")
        st.balloons()

# --- 7. THE CHAT INTERFACE (Pinned to Bottom) ---
if ai_enabled:
    # This loop shows the messages between the Lab and the Input box
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # This 'st.chat_input' is outside of any tabs/containers, 
    # so it stays pinned at the bottom of the screen.
    if prompt := st.chat_input("Ask the Universal Master...", accept_audio=True):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Trigger the response immediately
        with st.chat_message("assistant"):
            response = client.models.generate_content(
                model=MODEL_ID,
                contents=prompt,
                config=types.GenerateContentConfig(system_instruction=MASTER_CONTEXT)
            )
            st.markdown(response.text)
            st.session_state.messages.append({"role": "assistant", "content": response.text})
        st.rerun()
