import streamlit as st
import requests

# Hugging Face model endpoint (replace if needed)
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer YOUR_HUGGINGFACE_API_KEY"}  # free API key (or empty if public)

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Streamlit UI
st.title("Free Chatbot - Powered by HuggingFace GPT-2")

# Store chat messages in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Say something...")

if user_input:
    # Display user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Query the model
    with st.spinner("Thinking..."):
        output = query({"inputs": user_input})
        bot_response = output[0]["generated_text"] if isinstance(output, list) else "Sorry, I couldn't generate a response."

    # Display bot response
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)
