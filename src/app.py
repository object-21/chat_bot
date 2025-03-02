import streamlit as st
from utils import call_llama
st.title(':llama: Llama Chatbot')

st.caption("🚀 A Streamlit chatbot powered by  :llama: Llama")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

prompt = st.chat_input()
if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    with st.spinner('Generating response: '):
        msg = call_llama('deepseek-r1', prompt)['response']
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)