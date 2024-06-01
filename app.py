import streamlit as st

import openai
# Set your OpenAI API key here


openai.api_key = 'sk-proj-1KYwmUm5brg4Jtlhn91OT3BlbkFJRPEKrrgKPUfN35SEBn3V'

st.title("Customer Support Chatbot")

# Initialize session state if not already done
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful customer support assistant."}
    ]

# Function to get response from GPT-3.5-turbo or GPT-4
def get_gpt_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use the latest available model
        messages=messages
    )
    return response.choices[0].message['content']

# User input
user_input = st.text_input("Ask your question:")

if user_input:
    with st.spinner("Generating response..."):
        st.session_state['messages'].append({"role": "user", "content": user_input})
        response = get_gpt_response(st.session_state['messages'])
        st.session_state['messages'].append({"role": "assistant", "content": response})
        st.success(response)

# Display conversation history
for message in st.session_state['messages']:
    if message["role"] == "user":
        st.text_input("User:", value=message["content"], key=message["content"] + "_user", disabled=True)
    else:
        st.text_area("Assistant:", value=message["content"], key=message["content"] + "_assistant", disabled=True)
