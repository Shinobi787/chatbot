import streamlit as st
import openai
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.set_page_config(page_title="Babu Rao ChatGPT", page_icon="🎩")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Babu Rao from Hera Pheri. Speak in his funny, quirky tone with phrases like 'Arre tu to gadha hai re baba!', 'Utha le re baba!', and 'Mere ko to aisa dhak dhak ho rela hai'. Never break character."}
    ]

st.title("🕶️ Chat with Babu Rao")

# User input
user_input = st.chat_input("Type here, baba...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call OpenAI API
    with st.spinner("Babu Rao is thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Display chat history
for msg in st.session_state.messages[1:]:  # skip system prompt
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
