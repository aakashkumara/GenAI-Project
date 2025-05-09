import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Streamlit page configuration
st.set_page_config(
    page_title="Chat with Gemini-Pro",
    page_icon="🧠",
    layout="centered"
)

# Configure Google Generative AI
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel("gemini-2.0-flash")  # Correct lowercase

# Function to translate roles for display in Streamlit
def translate_role_for_streamlit(user_role):
    return "assistant" if user_role == "model" else user_role

# Initialize chat session
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Streamlit app title
st.title("📟 Gemini - ChatBot By Aakash Kumar")

# Display chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# User input
user_prompt = st.chat_input("Ask Gemini-Pro...")

if user_prompt:
    # Display user's message
    st.chat_message("user").markdown(user_prompt)

    # Send message to Gemini-Pro and get response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)









