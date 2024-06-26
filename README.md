
# LangChain-Google-Palm-EdTech-Query-System

### Project Overview

This project is an interactive Q&A system developed for an Ed-Tech platform using LangChain and Google Palm LLM (Gemini). The system leverages Hugging Face and FAISS for fast and accurate information retrieval and is designed with a user-friendly interface using Streamlit. The data is stored in CSV format, allowing for seamless database integration.

#### Tech Stack
-   **LangChain**
-   **Google Palm LLM (Gemini)**
-   **FAISS**
-   **Hugging Face**
-   **Streamlit**

### Features

-   **Interactive Q&A**
-   **Efficient Data Retrieval**
-   **User-Friendly Interface**
-   **CSV-Based Data Storage**

### Setup and Installation

#### Installation Steps

1.  **Clone the Repository**
        
    `git clone https://github.com/itsabhikhm/LangChain-Google-Palm-EduQuery-System.git`
   
2.  **Install Required Libraries**
   
    `pip install -r requirements.txt` 
    
3.  **Setup API Key**
    
    Edit the  `.env` file in the project directory and add your Google API key:
       
    `GOOGLE_API_KEY=your_key_here` 
    

### Running the Project

1.  **Run the Application**
        
    `python main.py` 
    
### Usage

The system can answer questions based on the context provided in the CSV file. It retrieves the most relevant information using the FAISS vector database and generates accurate responses with the help of Google's Gemini LLM.
