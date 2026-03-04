import streamlit as st
from agents import orchestrator
from google.adk.runners import InMemoryRunner
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Multi-Agent Coding Assistant",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
    .main {
        background-color: #0f1116;
        color: #e6edf3;
    }
    .stTextInput > div > div > input {
        background-color: #161b22;
        color: white;
        border: 1px solid #30363d;
    }
    .stButton > button {
        background-color: #238636;
        color: white;
        border-radius: 6px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .stButton > button:hover {
        background-color: #2ea043;
    }
    .agent-header {
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }
    .chat-bubble {
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1rem;
        border: 1px solid #30363d;
    }
    .user-bubble {
        background-color: #161b22;
    }
    .bot-bubble {
        background-color: #0d1117;
        border-left: 4px solid #4facfe;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="agent-header">Multi-Agent Coding Assistant</div>', unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

if "runner" not in st.session_state:
    st.session_state.runner = InMemoryRunner(orchestrator)
    try:
        st.session_state.runner.session_service.create_session_sync(
            app_name=st.session_state.runner.app_name,
            user_id="user_1",
            session_id="session_1"
        )
    except Exception:
        pass

if not os.getenv("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY") == "your_api_key_here":
    st.warning("Please set your `GOOGLE_API_KEY` in the `.env` file to start.")
    st.stop()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask Me Anything about Python, Java, or C++"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Orchestrating agents..."):
            try:
                content = types.Content(
                    role="user",
                    parts=[types.Part(text=prompt)]
                )
                
                events = st.session_state.runner.run(
                    user_id="user_1",
                    session_id="session_1",
                    new_message=content
                )
                
                full_response = ""
                for event in events:
                    if event.content and event.content.parts:
                        for part in event.content.parts:
                            if part.text:
                                full_response += part.text
                            elif part.function_call:
                                print(f"--- Calling Sub-Agent: {part.function_call.name} ---")
                
                if full_response:
                    st.markdown(full_response)
                    st.session_state.messages.append({"role": "assistant", "content": full_response})
                else:
                    st.warning("The orchestrator returned an empty response. This can happen if the sub-agent's response wasn't correctly propagated. Please try a more specific coding question.")
            except Exception as e:
                error_msg = f"An error occurred: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

with st.sidebar:
    st.title("About")
    st.write("This application uses **Google ADK** to orchestrate specialized LLM agents.")
    st.markdown("""
    **Expert Agents:**
    - 🐍 Python Expert
    - ☕ Java Expert
    - ⚙️ C++ Expert
    """)
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
