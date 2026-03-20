import streamlit as st
import random
import time

# --- HARMONY KNOWLEDGE BASE (THE FACTS) ---
HARMONY_FACTS = {
    "frequency": "The fundamental frequency of the Harmony Codex is 1420.405 MHz.",
    "null-g": "Null-G Propulsion uses mass-negation and inertia-cancellation to bypass classical Newtonian limits.",
    "pyro-stasis": "Pyro-Stasis uses molecular phase-locking to instantly neutralize thermal energy.",
    "sentinel": "The Sentinel Cell is a 10,000-year energy storage system with zero-entropy degradation.",
    "estate": "The T and C Estate is the paramount governing body for all Harmony-derived technologies.",
    "tlc": "The T.L.C. Shield is the master protocol for licensing and environmental governance."
}

# --- CHAT LOGIC ---
def get_harmony_response(prompt):
    """Simple Intelligence Engine: Matches user intent to Harmony Facts."""
    p = prompt.lower()
    if "frequency" in p or "mhz" in p:
        return HARMONY_FACTS["frequency"]
    elif "null" in p or "gravity" in p:
        return HARMONY_FACTS["null-g"]
    elif "fire" in p or "stasis" in p or "heat" in p:
        return HARMONY_FACTS["pyro-stasis"]
    elif "battery" in p or "energy" in p or "sentinel" in p:
        return HARMONY_FACTS["sentinel"]
    elif "who" in p or "owner" in p or "estate" in p:
        return HARMONY_FACTS["estate"]
    elif "shield" in p or "tlc" in p or "license" in p:
        return HARMONY_FACTS["tlc"]
    else:
        return "I am the Universal Master AI. Please ask about the Harmony Codex, Null-G, or the T.L.C. Shield."

# --- UI SETUP ---
st.set_page_config(page_title="Harmony Master AI", page_icon="🏛️")
st.title("🏛️ Universal Master AI")
st.write("---")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Master Handshake Confirmed. How can I assist the T and C Estate today?"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input (The Gemini-style box)
if prompt := st.chat_input("Ask about the Harmony Codex..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate assistant response
    response = get_harmony_response(prompt)
    
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        # Simulate "thinking" typewriter effect
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
