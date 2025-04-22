import streamlit as st
import requests
import json

class OllamaAPI:
    def __init__(self, base_url: str = "http://127.0.0.1:11434"):
        self.base_url = base_url

    def generate_response(self, prompt: str, model: str = "mistral:7b"):
        try:
            response = requests.post(
                f"{self.base_url}/api/generate",
                json={"model": model, "prompt": prompt, "stream": True},
                stream=True
            )
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    json_response = json.loads(line)
                    if chunk := json_response.get('response', ''):
                        yield chunk
        except Exception as e:
            yield f"Error: {str(e)}"

def initialize_chat():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "ollama_api" not in st.session_state:
        st.session_state.ollama_api = OllamaAPI()

def chatbot_ui():
    st.markdown("""
        <style>
        /* Chat container */
        .floating-chat-container {
            position: fixed;
            bottom: 20px;
            right: 20px;
            width: 350px;
            border-radius: 15px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            padding: 15px;
            # background: #f4f7fc;
            font-family: Arial, sans-serif;
        }

        /* Chat header */
        .chat-header {
            background: Gray;
            color: white;
            padding: 10px;
            border-radius: 15px 15px 0 0;
            text-align: center;
            font-weight: bold;
            font-size: 16px;
        }

        /* Chat body */
        .chat-body {
            max-height: 400px;
            overflow-y: auto;
            padding: 10px;
            display: flex;
            flex-direction: column;
        }

        /* Message container */
        .message-container {
            display: flex;
            margin-bottom: 5px;
        }

        /* Messages */
        .bot-message, .user-message {
            padding: 10px 15px;
            border-radius: 15px;
            font-size: 14px;
            max-width: 70%;
            word-wrap: break-word;
        }

        /* Bot messages (left side) */
        .bot-message {
            background: #D1E8FF;
            color: black;
            text-align: left;
            align-self: flex-start;
        }

        /* User messages (right side) */
        .user-message {
            background: #4A90E2;
            color: white;
            text-align: right;
            align-self: flex-end;
            margin-left: auto;  /* Pushes the user message to the right */
        }

        /* Input area */
        .chat-input {
            padding: 10px;
            background: white;
            border-top: 1px solid #ddd;
            border-radius: 0 0 15px 15px;
            text-align: center;
        }

        /* Input field */
        .chat-input input {
            width: 90%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 10px;
            font-size: 14px;
            outline: none;
        }
        </style>
    """, unsafe_allow_html=True)

    initialize_chat()

    with st.container():
        st.markdown('<div class="floating-chat-container">', unsafe_allow_html=True)
        st.markdown('<div class="chat-header">A safe space to talk!😄</div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-body">', unsafe_allow_html=True)
        
        for message in st.session_state.messages:
            message_class = "user-message" if message["role"] == "user" else "bot-message"
            alignment_class = "message-container user" if message["role"] == "user" else "message-container bot"
            st.markdown(f'<div class="{alignment_class}"><div class="{message_class}">{message["content"]}</div></div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)

        with st.markdown('<div class="chat-input">', unsafe_allow_html=True):
            user_input = st.text_input("How are you feeling today?", key="user_input")

            if user_input:
                st.session_state.messages.append({"role": "user", "content": user_input})
                full_response = ""
                for chunk in st.session_state.ollama_api.generate_response(user_input):
                    full_response += chunk
                
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                del st.session_state["user_input"]
                st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    chatbot_ui()
