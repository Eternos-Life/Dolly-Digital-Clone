import streamlit as st
from utils.rag import retrieve_context
from utils.llm import generate_response

# Set Streamlit page config
st.set_page_config(page_title="UARE.AI Dolly Assignment", layout="wide")

# App title
st.title("🐑 Dolly's Digital Twin")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome Baa-a-a-a-ck! I'm the digital twin of Dolly. What would you like to know?"}
    ]

# Display the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Text input for user query
user_input = st.chat_input("Ask me something about the customer...")

if user_input:
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Retrieve relevant context using RAG
    retrieved_docs = retrieve_context(user_input)

    # Generate response using LLM with chat history
    llm_response = generate_response(user_input, retrieved_docs, st.session_state.messages)

    # Add assistant message to history
    st.session_state.messages.append({"role": "assistant", "content": llm_response})
    with st.chat_message("assistant"):
        st.markdown(llm_response)
