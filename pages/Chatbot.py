import streamlit as st
import subprocess

# Set page title and icon
st.set_page_config(page_title="Query with Model", page_icon="🧠", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .user-message {
            background-color: #e1f5fe;
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
            text-align: right;
            display: inline-block;
            max-width: 80%;
            float: right;
        }
        .bot-response {
            background-color: #ffe0b2;
            border-radius: 5px;
            padding: 10px;
            margin: 10px 0;
            text-align: left;
            display: inline-block;
            max-width: 80%;
            float: left;
        }
        .title {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Title and description
st.markdown('<h1 class="title">Model Query Interface</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;">Choose a model and enter your query.</p>', unsafe_allow_html=True)

# Dropdown for selecting model
models = [
    "gemma2:2b",
    "phi3:latest",
    "llama3.2:1b",
    "mistral:latest",
    "llama3.2:latest"
]

# Initialize model selection in session state if it doesn't exist
if 'selected_model' not in st.session_state:
    st.session_state.selected_model = models[0]  # Default to the first model

# Update the selected model based on user choice
selected_model = st.selectbox("Choose a model:", models, index=models.index(st.session_state.selected_model))

# Update session state with the selected model
st.session_state.selected_model = selected_model

# Create a session state to keep track of chat history and input text
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'query_input' not in st.session_state:
    st.session_state.query_input = ""  # Initialize the input state

# Display chat history
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for query, response in st.session_state.chat_history:
        st.markdown(f'<div class="user-message"><strong>User:</strong> {query}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="bot-response"><strong>Bot:</strong> {response}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Text input for the query
query_text = st.text_input("Enter your query:", st.session_state.query_input, key="query_input", max_chars=500, placeholder="Type your message here...")

# Handle submission on Enter key
if query_text:
    if st.button("Submit", key="submit_button", help="Click to submit your query") or st.session_state.query_input != query_text:
        with st.spinner("Processing..."):
            # Call the backend script with the selected model and query text
            try:
                result = subprocess.run(
                    ['python', 'query_data.py', query_text, st.session_state.selected_model],
                    capture_output=True,
                    text=True,
                )

                # Show the response from the backend
                if result.returncode == 0:
                    response_text = result.stdout.strip()
                    response_text = response_text.split('Sources:')[0].strip()  # Keep only the response text
                    # Store the query and response in session state
                    st.session_state.chat_history.append((query_text, response_text))
                    # Clear the text input field
                    st.session_state.query_input = ""  # Clear the input field
                else:
                    st.error("Error in generating response")
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Update the session state only when the button is clicked or the input changes
if query_text != st.session_state.query_input:
    st.session_state.query_input = query_text  # Update session state with the current input
