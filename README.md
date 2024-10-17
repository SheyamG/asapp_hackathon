*ChatBot Project README*
*Overview*
  This project implements a chatbot that leverages document embeddings and retrieval-augmented generation (RAG) techniques. It allows users to upload documents, which are then processed and stored for efficient querying. The chatbot can respond to user queries by fetching relevant information from the stored documents.

*Table of Contents*
- Technologies Used
- Project Structure
- Setup Instructions
- Flow of the Project

*Technologies Used*
Python: Programming language for backend implementation.
Streamlit: Frontend framework for building web applications.
LangChain: Framework for handling document loading and text embeddings.
ChromaDB: Vector storage for efficient document retrieval.
Ollama: Model for generating embeddings and responses.

*Project Structure*
Chatbot-Final-Iteration/
├── data/                   # Directory for uploaded documents
│   populate_database.py # Script for populating the database
│   get_embedding_function.py # Function to get the embedding model
│   query_data.py       # Script for querying data
├── pages/
│   ├── Homepage.py         # Home page layout
│   ├── file_upload.py      # File upload interface
│   └── chatbot.py          # Chatbot interaction interface
├── requirements.txt        # Python package dependencies
└── README.md               # Project documentation

*Setup Instructions*
Clone the repository:
git clone <repository_url>
cd Chatbot-Final-Iteration

Install required packages:

pip install -r requirements.txt
Ensure that the data directory is correctly set up:

Create a data directory at N:/Sheyam/Chatbot-Final-Iteration/data for file uploads.

*Flow of the Project*
The data flow in this project can be divided into several key sections, each contributing to the overall functionality of the chatbot. Here’s how data moves through the application:

File Upload:

Users upload PDF documents via the File Upload page.
The files are temporarily held in memory and then saved to the designated data directory (N:/Sheyam/Chatbot-Final-Iteration/data).
After uploading, users receive a confirmation message indicating successful file storage.

Database Population:

When users click "Populate Database," the populate_database.py script is executed.
This script performs the following tasks:
Load Documents: It uses PyPDFDirectoryLoader to read and load all PDF files from the data directory into memory.
Split Documents: The loaded documents are processed using the RecursiveCharacterTextSplitter, which breaks them into smaller chunks suitable for embedding.
Embed and Store: Each chunk is passed to ChromaDB through the add_to_chroma function, where embeddings are calculated using the specified model. Only new chunks (not previously stored) are added to the database.
The data now resides in the ChromaDB, making it ready for retrieval during user queries.

Querying:

Users access the Chatbot interface to interact with the model.
When a user submits a query:
Retrieve Relevant Chunks: The query_data.py script is triggered, using the user's query to perform a similarity search in ChromaDB. It retrieves the top relevant document chunks based on their embeddings.
Generate Response: The context from the retrieved chunks is formatted into a prompt and sent to the selected model (e.g., Ollama) for generating a response.
The response, along with the sources of information (chunk IDs), is displayed back to the user in a conversational format.

Interaction History:

Throughout the user session, the chatbot maintains a history of interactions, storing each query and its corresponding response.
This allows users to view previous exchanges, facilitating a more engaging conversational experience.
