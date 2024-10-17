import os
import streamlit as st
import subprocess

# Define the folder where files will be uploaded
UPLOAD_FOLDER = 'N:/Sheyam/Chatbot-Final-Iteration/data'

# Create the upload folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def save_uploaded_file(uploaded_file):
    """Save the uploaded file to the designated folder."""
    try:
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        return file_path
    except Exception as e:
        st.error(f"Error saving file: {e}")
        return None

def list_uploaded_files():
    """List all uploaded files in the upload folder."""
    return [f for f in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))]

# Page layout and title
st.set_page_config(page_title="File Upload and Database Population", page_icon="📂", layout="centered")

# Title and description
st.markdown('<h1 style="text-align: center;">File Upload and Database Population</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center;">Upload your documents below and press "Done" to complete the upload.</p>', unsafe_allow_html=True)

# File uploader
uploaded_files = st.file_uploader("Upload Files", accept_multiple_files=True)

# Add a "Done" button to trigger the upload
if st.button("Done"):
    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_path = save_uploaded_file(uploaded_file)
            if file_path:
                st.success(f"File '{uploaded_file.name}' uploaded successfully and saved to {file_path}")
            else:
                st.error(f"Failed to upload file '{uploaded_file.name}'")
    else:
        st.warning("No files uploaded. Please upload files before pressing 'Done'.")

# Display uploaded files below the uploader
st.markdown('<h2 style="text-align: center;">Uploaded Documents</h2>', unsafe_allow_html=True)
uploaded_files_list = list_uploaded_files()

if uploaded_files_list:
    st.write("Here are the files you have uploaded:")
    for file in uploaded_files_list:
        st.markdown(f"- {file}")
else:
    st.write("No files have been uploaded yet.")

# Embedding model options (explicitly set to the specified model)
embedding_model = "nomic-embed-text:latest"

# Button to trigger the database population
if st.button("Populate Database"):
    with st.spinner("Populating database..."):
        # Run the populate script with the specified model
        command = [
            "python",
            "populate_database.py",  # Adjust this based on your actual script file
            "--model", embedding_model
        ]
        subprocess.run(command)
    st.success("Database populated successfully!")
