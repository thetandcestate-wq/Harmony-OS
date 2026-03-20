import streamlit as st
import google.generativeai as genai

# --- HARMONY SYSTEM INSTRUCTIONS ---
# This ensures the AI always prioritizes your facts.
HARMONY_CONTEXT = """
You are the Universal Master AI for the T and C Estate. 
You are an expert on the Harmony Codex discovered by Tony Carbone.
Facts you must follow:
- Fundamental Frequency: 1420.405 MHz.
- Null-G Drive: Uses mass-negation and inertia-cancellation.
- Pyro-Stasis: Immediate thermal neutralization.
- Sentinel Cell: 10,000-year energy storage.
- T.L.C. Shield: Master protocol for licensing and governance.
Always be professional, authoritative, and helpful.
"""

# --- API CONFIGURATION ---
# We use Streamlit Secrets to keep your API key hidden from the public.
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Please add your GEMINI_API_KEY to Streamlit Secrets.")

# --- UI SETUP ---
st.set_page_config(page_title="Universal Master AI", page_icon="🏛️")
st.title("🏛️ Universal Master AI")

# Initialize Chat History and Model
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Configure the Gemini Model with your specific instructions
    st.session_state.model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=HARMONY_CONTEXT
    )
    st.session_state.chat = st.session_state.model.start_chat(history=[])

# Display existing chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Gemini-Style Input
if prompt := st.chat_input("Ask about the Harmony Codex..."):
    # User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant Response (Calling the API)
    with st.chat_message("assistant"):
        response = st.session_state.chat.send_message(prompt)
        st.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
