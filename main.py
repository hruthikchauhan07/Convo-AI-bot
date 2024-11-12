#importing the required library

import os 
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

#loading env variables
load_dotenv()

#config page settings of streamlit
st.set_page_config(
    page_title="Chat to my personal AI",
    page_icon=":brain:",   #this is a favicon emoji
    layout="centered",
    
)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

#setting up the Google Gemini Pro AI model

gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

#function to translate roles bw Gemini Pro and Streamlit terminology usage

def trans_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

#initializing chat sessions in streamlit if not present already

if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])
    
    
#display the chatbot's title on page

st.title("Convo-AI 👾🌐 By Helix..")

#display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(trans_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)


#input field for user's message

user_prompt = st.chat_input("Ask Convo-AI...!")
if user_prompt:
    # adding user message to chat and displaying
    st.chat_message("user").markdown(user_prompt) 
    
    #send user message to gemini  and get response
    
    gemini_response = st.session_state.chat_session.send_message(user_prompt)
    
    #display gemini's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)