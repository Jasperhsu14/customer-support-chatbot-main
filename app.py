import streamlit as st

import openai
# Set your OpenAI API key here


openai.api_key = 'sk-proj-1KYwmUm5brg4Jtlhn91OT3BlbkFJRPEKrrgKPUfN35SEBn3V'

st.title("Customer Support Chatbot for Security Issues")

# 初始化 session state
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": (
            "You are a helpful customer support assistant specializing in cybersecurity issues. "
            "You are well-versed in topics like data encryption, network security, malware protection, "
            "phishing prevention, and privacy best practices. Provide thorough and accurate answers to "
            "any security-related questions."
        )}
    ]

# 獲取 GPT-3.5-turbo 或 GPT-4 的回應
def get_gpt_response(messages):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message.content

# 用戶輸入
user_input = st.text_input("Ask your cybersecurity question:")

# 將用戶輸入添加到對話歷史中並獲取回應
if user_input:
    with st.spinner("Generating response..."):
        # 添加用戶問題到對話歷史
        st.session_state['messages'].append({"role": "user", "content": user_input})
        
        # 生成回應
        response = get_gpt_response(st.session_state['messages'])
        
        # 添加回應到對話歷史
        st.session_state['messages'].append({"role": "assistant", "content": response})
        
        # 顯示回應
        st.success(response)

# 顯示對話歷史
for message in st.session_state['messages']:
    if message["role"] == "user":
        st.text_input("User:", value=message["content"], key=message["content"] + "_user", disabled=True)
    else:
        st.text_area("Assistant:", value=message["content"], key=message["content"] + "_assistant", disabled=True)